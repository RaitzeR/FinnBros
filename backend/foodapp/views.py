from django.shortcuts import render
from django.views.generic import TemplateView
from foodapp.models import FoodPost, Category
from foodapp.helpers import *
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
import json
from django.db import IntegrityError

def index(request):
    return render(request, 'index.html', {

    })

def get_img_categories(request):
    url = request.GET.get("image_url")
    imageClasses = ImageClasses(image_url=url, threshold="0.5")
    classes = imageClasses.classes

    jsonresp = JsonResponse(classes, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

def categories_to_food_posts(request):
    pass

def get_food_posts(request):
    food_posts = FoodPost.objects.all()
    food_posts_json = serialize('json', food_posts)

    jsonresp = JsonResponse(food_posts_json, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

def create_food_post(request):
    title = request.GET.get("title")

    try:
        new_food_post = FoodPost(title=title)
        new_food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def edit_food_post(request):
    title = request.GET.get("title")
    id = request.GET.get("id")

    try:
        food_post = FoodPost.objects.get(pk=int(id))
        food_post.title = title
        food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def delete_food_post(request):
    id = request.GET.get("id")

    try:
        food_post = FoodPost.objects.get(pk=int(id))
        food_post.delete()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

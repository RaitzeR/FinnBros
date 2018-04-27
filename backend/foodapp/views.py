from django.shortcuts import render
from django.views.generic import TemplateView
from foodapp.models import Food, FoodCategory
from foodapp.helpers import *
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
import json
from django.db import IntegrityError

def index(request):
    return render(request, 'index.html', {

    })

# Give image categories to front-end
def get_img_categories(request):
    url = request.GET.get("image_url")
    imageClasses = ImageClasses(image_url=url, threshold="0.5")
    classes = imageClasses.classes

    jsonresp = JsonResponse(classes, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return jsonresp

# Attach categories to food post. Front-end gives category name in array
def categories_to_food_post(request):
    cat_titles = request.GET.getlist("category_titles[]")
    post_id = request.GET.get("post_id")

    for cat in cat_titles:
        post_to_attach = Food.get.objects(pk=int(post_id))
        try:
            cat_to_attach = FoodCategory.objects.get(title=cat)
        except FoodCategory.ObjectNotFound:
            cat_to_attach = Category(title=cat)
            cat_to_attach.save()
        post_to_attach.categories.add(cat_to_attach)

# List all posts to front-end
def get_food_posts(request):
    food_posts = Food.objects.all()
    food_posts_json = serialize('json', food_posts)

    jsonresp = JsonResponse(food_posts_json, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

# Create post
def create_food_post(request):
    title = request.GET.get("title")

    try:
        new_food_post = Food(title=title)
        new_food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

# Edit post
def edit_food_post(request):
    title = request.GET.get("title")
    id = request.GET.get("id")

    try:
        food_post = Food.objects.get(pk=int(id))
        food_post.title = title
        food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

# Delete post
def delete_food_post(request):
    id = request.GET.get("id")

    try:
        food_post = Food.objects.get(pk=int(id))
        food_post.delete()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

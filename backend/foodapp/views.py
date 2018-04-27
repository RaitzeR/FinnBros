from django.shortcuts import render
from django.views.generic import TemplateView
from foodapp.models import FoodPost
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
import json
from urllib.parse import urlparse
from django.db import IntegrityError
from Vision import ImageClasses


def get_referrer_root(request):
    try:
        # If getting from outside heroku, get referrer_root and allow in CORS
        parsed = urlparse(request.META['HTTP_REFERER'])
        referrer_root = parsed.scheme + "://" + parsed.netloc
    except KeyError:
        referrer_root = ""
    return referrer_root


def index(request):
    return render(request, 'index.html', {

    })


def get_food_posts(request):
    food_posts = FoodPost.objects.all()
    food_posts_json = serialize('json', food_posts)

    jsonresp = JsonResponse(food_posts_json, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp


def create_food_post(request):
    title = request.POST.get("title")

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

<<<<<<< HEAD
def edit_food_post(request):
    title = request.POST.get("title")
    id = request.POST.get("id")

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
    id = request.POST.get("id")

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
=======

def classify_image(request):
    url = request.POST.get("image_url")
    imageClasses = ImageClasses(image_url=url, threshold="0.5")
    classes = imageClasses.classes
>>>>>>> e314433b3e38aba0a9bfaf1fbd3d19fcae4a8b38

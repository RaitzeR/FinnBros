from foodapp.models import Food
from foodapp.views.helpers import *
from foodapp.geolocate import GeoLocate
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
#import json

# List all posts to front-end
def food_get_all(request):
    from django.core.serializers import serialize
    food_posts = Food.objects.all()
    food_posts_json = serialize('json', food_posts)

    jsonresp = JsonResponse(food_posts_json, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

def food_get(request):
    pass

def food_buy(request):
    buyer_id = request.GET.get("buyer_id")
    post_id = request.GET.get("id")

    try:
        food_post = Food.objects.get(pk=int(id))
        food_post.is_bought = True
        food_post.buyer = buyer_id
        food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def food_create(request):
    title = request.GET.get("title")
    image_url = request.GET.get("image_url")
    owner = request.GET.get("owner")
    street_address = request.GET.get("street_address")
    city = request.GET.get("city")
    country = request.GET.get("country")

    geoLocate = GeoLocate(address=street_address,city=city,country=country)
    longitude = geoLocate.geocode["lng"]
    latitude = geoLocate.geocode["lat"]

    try:
        new_food_post = Food(
            title=title,
            image_url=image_url,
            owner=owner,
            street_address=street_address,
            city=city,
            country=country,
        )
        new_food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def food_edit(request):
    title = request.GET.get("title")
    image_url = request.GET.get("image_url")
    owner = request.GET.get("owner")
    street_address = request.GET.get("street_address")
    city = request.GET.get("city")
    country = request.GET.get("country")
    id = request.GET.get("id")

    if street_address and city and country:
        geoLocate = GeoLocate(address=street_address, city=city, country=country)
        longitude = geoLocate.geocode["lng"]
        latitude = geoLocate.geocode["lat"]
    
    try:
        food_post = Food.objects.get(pk=int(id))
        food_post.title = title
        food_post.image_url = image_url
        food_post.owner = owner
        food_post.street_address = street_address
        food_post.city = city
        food_post.country = country
        food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def food_delete(request):
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

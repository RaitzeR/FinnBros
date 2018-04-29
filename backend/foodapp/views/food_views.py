from foodapp.models import Food, FirebaseUser, Community
from foodapp.views.helpers import *
from foodapp.geolocate import GeoLocate
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.core.serializers import serialize
import datetime
import json
#import pdb; pdb.set_trace()
#from pprint import pprint;pprint()

# List all posts to front-end
def food_get_all(request):
    food_posts = Food.objects.all()
    food_posts_json = serialize('json', food_posts)
    jsonresp = JsonResponse(food_posts_json, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

def food_get(request):
    id = request.GET.get("id")

    food = Food.objects.filter(pk=int(id))
    # User not found
    if len(food) == 0:
        jsonresp = JsonResponse({"error": "not found"}, safe=False)
        jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return jsonresp

    food_json = json.loads(serialize('json', food))

    category_list = []
    for cat in food[0].categories.all():
        dict_to_add = {}
        dict_to_add["id"] = cat.pk
        dict_to_add["title"] = cat.title
        category_list.append(dict_to_add)

    food_json[0]["fields"]["categories"] = category_list
    food_json[0]["fields"]["user"] = food[0].user.firebase_id
    jsonresp = JsonResponse(food_json, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

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
    user = FirebaseUser.objects.get(firebase_id=owner)
    community = request.GET.get("community")
    community = Community.objects.get(pk=int(community))
    street_address = request.GET.get("street_address")
    city = request.GET.get("city")
    country = request.GET.get("country")
    expiry = request.GET.get("expiry")
    price = request.GET.get("price")

    expiry = datetime.datetime.strptime(expiry, "%d.%m.%Y").date()

    geoLocate = GeoLocate(address=street_address,city=city,country=country)
    longitude = geoLocate.geocode["lng"]
    latitude = geoLocate.geocode["lat"]

    try:
        new_food_post = Food(
            title=title,
            image_url=image_url,
            user=user,
            street_address=street_address,
            latitude=latitude,
            longitude=longitude,
            community=community,
            city=city,
            price=price,
            country=country,
            expiry=expiry
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
    user = FirebaseUser.objects.get(firebase_id=owner)
    community = request.GET.get("community")
    community = Community.objects.get(pk=int(community))
    street_address = request.GET.get("street_address")
    city = request.GET.get("city")
    country = request.GET.get("country")
    id = request.GET.get("id")
    expiry = request.GET.get("expiry")
    price = request.GET.get("price")

    expiry = datetime.datetime.strptime(expiry, "%d.%m.%Y").date()

    if street_address and city and country:
        geoLocate = GeoLocate(address=street_address, city=city, country=country)
        longitude = geoLocate.geocode["lng"]
        latitude = geoLocate.geocode["lat"]

    try:
        food_post = Food.objects.get(pk=int(id))
        food_post.title = title
        food_post.image_url = image_url
        food_post.owner = user
        food_post.price = price
        food_post.street_address = street_address
        food_post.latitude = latitude
        food_post.longitude = longitude
        food_post.city = city
        food_post.community = community
        food_post.country = country
        food_post.expiry = expiry
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

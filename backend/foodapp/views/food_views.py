from foodapp.models import Food, FirebaseUser
from foodapp.views.helpers import *
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.core.serializers import serialize
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
    food_json = json.loads(serialize('json', food))

    category_list = []
    for cat in food[0].categories.all():
        dict_to_add = {}
        dict_to_add["id"] = cat.pk
        dict_to_add["title"] = cat.title
        category_list.append(dict_to_add)

    food_json[0]["fields"]["categories"] = category_list
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
    user = FirebaseUser.objects.get(firebase_id=int(owner))
    street_address = request.GET.get("street_address")
    city = request.GET.get("city")
    country = request.GET.get("country")

    try:
        new_food_post = Food(
            title=title,
            image_url=image_url,
            user=owner,
            street_address=street_address,
            city=city,
            country=country
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

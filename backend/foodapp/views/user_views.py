from django.db import IntegrityError
from foodapp.models import FirebaseUser, UserRating
from django.http import HttpResponse, JsonResponse
from foodapp.views.helpers import *
from django.core.serializers import serialize

def user_create(request):
    id = request.GET.get("id")

    try:
        new_user = FirebaseUser(firebase_id=id)
        new_user.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def user_get(request):
    id = request.GET.get("id")
    user = FirebaseUser.objects.filter(firebase_id=id)

    # User not found
    if len(user) == 0:
        jsonresp = JsonResponse({"error": "user not found"}, safe=False)
        jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return jsonresp

    user_foods = user[0].food_set.all()
    user_comms = user[0].community_set.all()

    user_json = serialize('json', user)
    user_foods_json = serialize('json', user_foods)
    user_comms_json = serialize('json', user_comms)

    data = {
        "user": user_json,
        "user_foods":user_foods_json,
        "user_comms":user_comms_json
    }

    jsonresp = JsonResponse(data, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

def user_delete(request):
    id = request.GET.get("id")

    try:
        user = FirebaseUser.objects.get(firebase_id=id)
        user.delete()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def user_get_rating(request):
    id = request.GET.get("id")

    try:
        ratings = UserRating.objects.get(rated=id)
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    rating_count = 0
    total_rating = 0
    for rating in ratings:
        rating_count = rating_count + 1
        total_rating = total_rating + rating.rating

    mean_rating = total_rating / rating_count
    return mean_rating

def rate_user(request):
    rator = request.GET.get("rator")
    rated = request.GET.get("rated")
    rating = request.GET.get("rating")

    try:
        new_rating = UserRating(rator=rator,rated=rated,rating=rating)
        new_rating.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp
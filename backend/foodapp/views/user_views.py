from django.db import IntegrityError
from foodapp.models import FirebaseUser
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
    user = FirebaseUser.objects.filter(firebase_id=int(id))

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
        user = FirebaseUser.objects.get(firebase_id=int(id))
        user.delete()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

from django.db import IntegrityError
from foodapp.models import Community, FirebaseUser
from django.http import HttpResponse, JsonResponse
import json
from foodapp.views.helpers import *
from django.core.serializers import serialize

def community_create(request):
    title = request.GET.get("title")
    description = request.GET.get("description")
    is_public = request.GET.get("is_public")

    try:
        new_comm = Community(
            title=title,
            description=description,
            is_public=json.loads(is_public),
        )
        new_comm.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def community_get(request):
    id = request.GET.get("id")
    comm = Community.objects.filter(pk=int(id))

    #  not found
    if len(comm) == 0:
        jsonresp = JsonResponse({"error": "not found"}, safe=False)
        jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return jsonresp

    #comm_foods = user[0].food_set.all()
    #comm_users = user[0].community_set.all()

    comm_json = serialize('json', comm)
    comm_foods_json = ["work in progress"]
    comm_users_json = ["work in progress"]

    data = {
        "comm": comm_json,
        "comm_foods":comm_foods_json,
        "comm_users":comm_users_json
    }

    jsonresp = JsonResponse(data, safe=False)
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)

    return jsonresp

def community_delete(request):
    id = request.GET.get("id")

    try:
        comm = Community.objects.get(pk=int(id))
        comm.delete()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def community_edit(request):
    title = request.GET.get("title")
    description = request.GET.get("description")
    is_public = request.GET.get("is_public")

    try:
        comm = Community.objects.get(pk=int(id))
        comm.title = title
        comm.description = description
        comm.is_public = json.dumps(is_public)
        food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def community_join_user(request):
    comm_id = request.GET.get("id")
    user_id = request.GET.get("user_id")

    community = Community.objects.get(pk=int(comm_id))
    user = FirebaseUser.objects.get(firebase_id=user_id)
    community.users.add(user)

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def community_leave_user(request):
    comm_id = request.GET.get("id")
    user_id = request.GET.get("user_id")

    community = Community.objects.get(pk=int(comm_id))
    user = FirebaseUser.objects.get(firebase_id=user_id)
    community.users.remove(user)

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def community_create(request):
    title = request.GET.get("title")
    description = request.GET.get("description")
    is_public = request.GET.get("is_public")

    try:
        new_cat = FoodCategory(
            title=title,
            description=description,
            is_public=json.dumps(is_public),
        )
        new_food_post.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def community_get(request):
    pass

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
    user = FirebaseUser.objects.get(pk=int(user_id))
    community.users.add(user)

    resp = HttpResponse(200)

def community_leave_user(request):
    comm_id = request.GET.get("id")
    user_id = request.GET.get("user_id")

    community = Community.objects.get(pk=int(comm_id))
    user = FirebaseUser.objects.get(pk=int(user_id))
    community.users.remove(user)

    resp = HttpResponse(200)

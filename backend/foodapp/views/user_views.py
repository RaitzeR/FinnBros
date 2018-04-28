def user_create(request):
    try:
        new_user = FirebaseUser()
        new_user.save()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

def user_get(request):
    pass

def user_delete(request):
    id = request.GET.get("id")

    try:
        user = FirebaseUser.objects.get(pk=int(id))
        user.delete()
    except IntegrityError as e:
        resp = JsonResponse({"message": e.args})
        resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
        return resp

    resp = HttpResponse(200)
    resp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    return resp

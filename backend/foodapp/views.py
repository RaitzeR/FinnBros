from django.shortcuts import render
from django.views.generic import TemplateView
from foodapp.models import FoodPost
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
import json
from urllib.parse import urlparse

def index(request):
    return render(request, 'index.html', {

    })

def get_food_posts(request):
    food_posts = FoodPost.objects.all()
    food_posts_json = serialize('json', food_posts)

    jsonresp = JsonResponse(food_posts_json, safe=False)
    try:
        # If getting from outside heroku, get referrer_root and allow in CORS
        parsed = urlparse(request.META['HTTP_REFERER'])
        referrer_root = parsed.scheme + "://" + parsed.netloc
        jsonresp['Access-Control-Allow-Origin'] = referrer_root
    except KeyError:
        pass

    return jsonresp

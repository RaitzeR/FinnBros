from django.shortcuts import render
from django.views.generic import TemplateView
from foodapp.models import FoodPost
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    return render(request, 'index.html', {

    })

def get_food_posts(request):
    food_posts = FoodPost.objects.all()
    food_posts_json = serialize('json', food_posts)
    return JsonResponse(food_posts_json, safe=False)

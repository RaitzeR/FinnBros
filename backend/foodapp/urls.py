from django.conf.urls import url
from foodapp import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
    path('', views.index),
    path('get_food_posts/', views.get_food_posts),
    path('create_food_post/', views.create_food_post),
]

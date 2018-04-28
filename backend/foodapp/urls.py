from django.conf.urls import url
from foodapp import views
from django.urls import path
from foodapp import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
    path('', views.index),
    path('food/get', views.food_get),
    path('food/get/all', views.food_get_all),
    path('food/create', views.food_create),
    path('food/edit', views.food_edit),
    path('food/buy', views.food_buy),
    path('food/delete', views.food_delete),
    path('community/create', views.community_create),
    path('community/get', views.community_get),
    path('community/delete', views.community_delete),
    path('community/edit', views.community_edit),
    path('community/join_user', views.community_join_user),
    path('community/leave_user', views.community_leave_user),
    path('watson/img_categories', views.img_categories),
    path('category/categories_to_food/', views.categories_to_food),
]

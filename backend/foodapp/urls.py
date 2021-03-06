from django.conf.urls import url
from foodapp import views
from django.urls import path
from foodapp import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
    path('', views.index),
    path('user/create', views.user_create),
    path('user/get', views.user_get),
    path('user/delete', views.user_delete),
    path('user/get_rating', views.user_get_rating),
    path('user/rate', views.rate_user),
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
    path('category/categories_to_food/', views.categories_to_food),
    path('category/remove_categories/', views.remove_categories),
    path('watson/img_categories', views.img_categories),
]

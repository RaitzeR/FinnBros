from django.conf.urls import url
from foodapp import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
    path('', views.index),
    url(r'^links/$' , views.LinksPageView.as_view()),
]

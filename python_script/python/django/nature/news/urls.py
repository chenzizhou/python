from django.contrib import admin
from django.urls import path, re_path
from .views import news_views

urlpatterns = [
    re_path(r'^$',news_views),
]
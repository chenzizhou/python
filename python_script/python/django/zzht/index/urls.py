from audioop import add
from django.urls import re_path,path
from .views import *
urlpatterns=[
    re_path('^add/$',add_view),
    re_path('addEmployee',addEmployee_view,name='add'),
    re_path('setSession',setSession_view),
    re_path('getSession',getSession_view),


]
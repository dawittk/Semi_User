from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
   
    url(r'^index/$', views.index , name= "index"),
    url(r'^create/$', views.create , name= "create"),
    url(r'^success/$', views.success , name= "success"),
    url(r'^show/(?P<id>\d+)$', views.show , name= "show"),
    url(r'^update/(?P<id>\d+)$', views.update , name= "update"),
    url(r'^delete/(?P<id>\d+)/$', views.delete , name= "delete"),
]

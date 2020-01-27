from django.conf.urls import url
from django.urls import path,re_path,include
from .views import parametertypeview

urlpatterns = [
    path('',parametertypeview)
]
from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    path('notification/', "views.ListofNotification")
]
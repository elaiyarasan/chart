from django.http import HttpResponse
from django.shortcuts import render
from .forms import notificationForm
from .models import notification
from .serializers import NotificationSerializer
from rest_framework import viewsets, permissions
from . import serializers

# Create your views here.
def notification_not(request):
    notification_not_list = notification.objects.order_by('id')
    notification_not=notificationForm()
    if request.method=="POST":
        notification_not=notificationForm(request.POST)
    if notification_not.is_valid():
        notification.objects.create(**notification_not.cleaned_data)        
    return render(request,"notification/notification.html",{"form":notification_not,'notification_not_list':notification_not_list})
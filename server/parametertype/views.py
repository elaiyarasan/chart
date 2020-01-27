from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import ParametertypeSerializer
# Create your views here.

def parametertypeview(request):
       return HttpResponse('text')
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def koushik(request):
    return HttpResponse("Hello Koushik")

def ananymous(request, name):
    return HttpResponse("Hello " + name + " welcome to our website")
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # second changes
    return render(request,"index.html")


def koushik(request):
    return HttpResponse("Hello Koushik")

def ananymous(request, name):
    return HttpResponse("Hello " + name + " welcome to our website")

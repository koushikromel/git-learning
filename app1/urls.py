from django.urls import path
from .import views
from  app1 import views

urlpatterns = [
    path('',views.index, name='index')
]
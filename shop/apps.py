#from django.apps import AppConfig
from django.shortcuts import render
from django.http import HttpResponse


# class ShopConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'shop'
def shop(request):
    return HttpResponse("Hello world!")

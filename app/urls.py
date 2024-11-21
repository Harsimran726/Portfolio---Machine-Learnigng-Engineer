
from django.contrib import admin
from django.urls import path , include
from app import views
from .views import *


urlpatterns = [
    path("",views.home,name='Home')
]

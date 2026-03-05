from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.address_book, name="address_book"),
    
]

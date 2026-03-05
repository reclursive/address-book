from django.urls import path
from . import views 

urlpatterns = [
    path('', views.address_book_view, name='address_book'),  
]
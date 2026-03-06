from django.urls import path
from . import views

urlpatterns = [
    path('', views.address_book_view, name='address_book'),
    path('contact/<int:contact_id>/', views.address_book_view, name='contact_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('address_book.urls')), 
    path('admin/', admin.site.urls),
]
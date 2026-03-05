from django.contrib import admin
from django.urls import path, include  # include lets the app handle its URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('address_book.urls')),  
]
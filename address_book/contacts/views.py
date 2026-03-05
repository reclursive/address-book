from django.shortcuts import render

def address_book(request):
    return render(request, "address_book.html")
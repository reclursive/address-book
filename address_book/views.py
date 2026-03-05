from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def address_book_view(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()  # saves to SQLite
            return redirect('address_book')

    else:
        form = ContactForm()

    contacts = Contact.objects.all()

    return render(request, "address_book/address_book.html", {
        "form": form,
        "contacts": contacts
    })
    
    form.save()
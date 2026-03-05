from django.shortcuts import render, redirect
from .models import Contact, Email
from .forms import ContactForm


def address_book_view(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            email_value = request.POST.get("email")

            if email_value:
                Email.objects.create(
                    contact=contact,
                    email=email_value
                )

            return redirect("address_book")

    else:
        form = ContactForm()

    contacts = Contact.objects.all()

    return render(request, "address_book/address_book.html", {
        "form": form,
        "contacts": contacts
    })
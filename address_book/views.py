from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Email
from .forms import ContactForm


def address_book_view(request, contact_id=None):
    selected_contact = None
    emails = []

    # Load selected contact if provided
    if contact_id:
        selected_contact = get_object_or_404(Contact, id=contact_id)
        emails = selected_contact.emails.all()
        form = ContactForm(instance=selected_contact)
    else:
        form = ContactForm()

    if request.method == "POST":

        # ->save
        if "save_contact" in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                new_contact = form.save()
                return redirect("contact_detail", contact_id=new_contact.id)

        # ->add email to just the currently selected contact

        elif "add_email" in request.POST:
            email_value = request.POST.get("email")
            contact_id_post = request.POST.get("contact_id")
            if contact_id_post and email_value:
                contact = get_object_or_404(Contact, id=contact_id_post)
                Email.objects.create(contact=contact, email=email_value)
            return redirect("contact_detail", contact_id=contact_id_post)

        # ->remove contact all together
        elif "delete_contact" in request.POST:
            contact_id_post = request.POST.get("contact_id")
            if contact_id_post:
                contact = get_object_or_404(Contact, id=contact_id_post)
                contact.delete()
            return redirect("address_book")

    contacts = Contact.objects.all().order_by("first_name", "last_name")

    return render(
        request,
        "address_book/address_book.html",
        {
            "contacts": contacts,
            "form": form,
            "selected_contact": selected_contact,
            "emails": emails,
        },
    )
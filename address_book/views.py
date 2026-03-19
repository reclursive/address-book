# address_book/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Email
from .forms import ContactForm

def address_book_view(request, contact_id=None):
    selected_contact = None
    emails = []

    # POST reqs

    if request.method == "POST":

        #clear form
        if "clear_form" in request.POST:
            return redirect("address_book")

        #save/create 
        elif "save_contact" in request.POST:
            selected_contact_instance = None
            if contact_id:
                selected_contact_instance = get_object_or_404(Contact, id=contact_id)

            form = ContactForm(request.POST, instance=selected_contact_instance)
            if form.is_valid():
                contact = form.save()
                # Add email if provided
                email_value = request.POST.get("email")
                if email_value:
                    Email.objects.create(contact=contact, email=email_value)
                return redirect("contact_detail", contact_id=contact.id)

        # add additional email to already established contact
        elif "add_email" in request.POST:
            email_value = request.POST.get("email")
            contact_id_post = request.POST.get("contact_id")
            if contact_id_post and email_value:
                contact = get_object_or_404(Contact, id=contact_id_post)
                Email.objects.create(contact=contact, email=email_value)
            return redirect("contact_detail", contact_id=contact_id_post)

        # delete contact 
        elif "delete_contact" in request.POST:
            contact_id_post = request.POST.get("contact_id")
            if contact_id_post:
                contact = get_object_or_404(Contact, id=contact_id_post)
                contact.delete()
            return redirect("address_book")

        # delete one email
        
        elif "delete_email" in request.POST:
            email_id = request.POST.get("delete_email")
            contact_id_post = request.POST.get("contact_id")

            if email_id:
                email = get_object_or_404(Email, id=email_id, contact_id=contact_id_post)
                email.delete()

            return redirect("contact_detail", contact_id=contact_id_post)

 #get reqs
    if contact_id:
        selected_contact = get_object_or_404(Contact, id=contact_id)
        emails = selected_contact.emails.all()
        form = ContactForm(instance=selected_contact)
    else:
        form = ContactForm()


    # grabbing contacts for sidebar
    contacts = Contact.objects.only('id', 'first_name', 'last_name', 'big_fan') \
                              .order_by('-big_fan', 'first_name', 'last_name')

    # rendering
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
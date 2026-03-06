from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=False) 

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email']
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'Birthday'
        })
    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'big_fan', 'birthday']
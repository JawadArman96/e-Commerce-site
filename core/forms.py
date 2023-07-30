from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('Stripe', 'Stripe'),
    ('Paypal', 'Paypal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '123 Main St'
    }))
    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apartment or Suite'
    }))
    country = CountryField(blank_label="Choose...").formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',  # 'custom-select d-block w-100',
        })
    )
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'zip'
    }))
    same_billing_address = forms.BooleanField(required=False)  # widget=forms.CheckboxInput()
    save_info = forms.BooleanField(required=False)  # widget=forms.CheckboxInput()
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES
    )

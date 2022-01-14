from django import forms
from .models import Order


# this is based on CI video Checkouts - Part 4
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # these fields are the same as in models/Order
        fields = (
            'full_name', 'email', 'phone_number', 
            'street_address1', 'street_address2', 
            'town_or_city', 'postcode',
            'country', 'county',)
              
    def __init__(self, *args, **kwargs):
        """
        Adds placeholders to the form fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # the line below means the users cursor will start in this field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                # the line below sets the placeholder attributes that were created above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # the below is a css class, so adjust in main.css 
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
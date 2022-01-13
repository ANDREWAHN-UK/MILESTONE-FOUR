from django import forms
from store.models import Product, Category, Review

class ProductAdminForm(forms.ModelForm):
    """ ModelForm class to validate product instance data before saving from admin interface """
    class Meta:
        model = Product
        fields = '__all__'
     
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError(
                'Price supplied must be greater than zero.'
                )
        return self.cleaned_data['price']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ A simple form to allow users to leave reviews """
    
    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
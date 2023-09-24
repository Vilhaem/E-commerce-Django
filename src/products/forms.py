from django import forms
from .models import Product

input_css_class = "form-control"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'handle', 'price']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'handle': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

from django import forms
from .models import Product

input_css_class = "form-control"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'handle', 'price']

        widgets = {
            'name': forms.TextInput(attrs={'class': input_css_class}),
            'handle': forms.TextInput(attrs={'class': input_css_class}),
            'price': forms.NumberInput(attrs={'class': input_css_class, 'step': '0.01'}),
        }
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image','name', 'handle', 'price']

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': input_css_class}),
            'handle': forms.TextInput(attrs={'class': input_css_class}),
            'price': forms.NumberInput(attrs={'class': input_css_class, 'step': '0.01'}),
        }
    

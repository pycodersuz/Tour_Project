from django import forms
from .models import Tour, AirCategory

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'description', 'image', 'price', 'category',]

class AirCategoryForm(forms.ModelForm):
    class Meta:
        model = AirCategory
        fields = ['name', 'price']


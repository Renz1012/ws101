# cars/forms.py
from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_id', 'car_name', 'car_brand', 'car_type', 'car_year']  # Use the correct fields here

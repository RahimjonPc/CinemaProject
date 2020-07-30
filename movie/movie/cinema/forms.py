from .models import Booking
from django.forms import ModelForm, TextInput, NumberInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name_customer', 'name_movie', 'customer_seats']
        Enter = {
            "name_customer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            "customer_seats": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select seat'
            }),
            "name_movie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name movie'
            }),
        }
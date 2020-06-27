from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'publish',  'service', 'first_name',
                        'last_name', 'email', 'mob_number', 'message',]

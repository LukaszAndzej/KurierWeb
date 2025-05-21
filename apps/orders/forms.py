from django import forms
from .models import Order, Parcel, Address

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = [
            'recipient_name', 'recipient_email', 'recipient_phone',
            'recipient_street', 'recipient_house_number',
            'recipient_postal_code', 'recipient_city', 'pickup_point', 'size', 'weight'
        ]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'street', 'city', 'postal_code', 'country']

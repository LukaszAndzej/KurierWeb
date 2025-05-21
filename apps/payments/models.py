from django.db import models
from apps.orders.models import Order

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('CARD', 'Karta płatnicza'),
        ('PAYPAL', 'PayPal'),
        ('BLIK', 'BLIK'),
        ('COD', 'Za pobraniem'),
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='CARD')
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Płatność {self.pk} ({self.get_method_display()})"

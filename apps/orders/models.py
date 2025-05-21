from django.db import models
from django.conf import settings
from geopy.geocoders import Nominatim
import uuid

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    tracking_number = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    status = models.CharField(
        max_length=20,
        choices=[
            ('NEW', 'Nowe'),
            ('PICKED_UP', 'Kurier odebrał paczkę'),
            ('SORTING', 'Paczka jest na sortowni'),
            ('OUT_FOR_DELIVERY', 'Wydana do doręczenia'),
            ('DELIVERED', 'Doręczona'),
        ],
        default='NEW'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='order_addresses',
    )
    full_name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

class Parcel(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='parcel')
    recipient_name = models.CharField(max_length=100)
    recipient_email = models.EmailField(default="default@example.com")
    recipient_phone = models.CharField(max_length=20, default="000-000-000")
    recipient_street = models.CharField(max_length=200, default="Nieznany adres")  # Ulica
    recipient_house_number = models.CharField(max_length=10, default="0")
    recipient_postal_code = models.CharField(max_length=10, default="00-000")
    recipient_city = models.CharField(max_length=100, default="Kraków")
    size = models.CharField(max_length=20, default="Nieznany rozmiar")
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    pickup_point = models.CharField(max_length=100, choices=[
        ('KRAKOW_1', 'Punkt Kraków 1 - ul. Rynek Główny 1'),
        ('KRAKOW_2', 'Punkt Kraków 2 - ul. Floriańska 15'),
        ('KRAKOW_3', 'Punkt Kraków 3 - ul. Kazimierz 12'),
    ])
    recipient_coordinates = models.JSONField(null=True, blank=True)
    current_lat = models.FloatField(null=True, blank=True)  # Aktualne szerokość geograficzna
    current_lng = models.FloatField(null=True, blank=True)  # Aktualna długość geograficzna

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="courier_project")
        location = geolocator.geocode(
            f"{self.recipient_street}, {self.recipient_city}, {self.recipient_postal_code}"
        )
        if location:
            self.recipient_coordinates = {'lat': location.latitude, 'lng': location.longitude}
        super().save(*args, **kwargs)

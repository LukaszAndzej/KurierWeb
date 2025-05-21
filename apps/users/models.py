from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Rozszerzony model użytkownika.
    Pola: 'is_business', 'nip' itp.
    """
    is_business = models.BooleanField(default=False)
    nip = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username

class Address(models.Model):
    """
    Adres przypisany do użytkownika.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=100)
    building_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=100, default='Polska')

    def __str__(self):
        return f"{self.street} {self.building_number}, {self.city}"

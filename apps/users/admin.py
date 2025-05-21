from django.contrib import admin
from .models import User, Address

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_business', 'nip')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'postal_code', 'country')

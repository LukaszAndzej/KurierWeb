from django.contrib import admin
from .models import Parcel, Order

class ParcelAdmin(admin.ModelAdmin):
    list_display = ['recipient_name', 'size', 'weight']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'status', 'created_at']

admin.site.register(Parcel, ParcelAdmin)
admin.site.register(Order, OrderAdmin)

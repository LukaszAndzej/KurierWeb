from django.db import models
from apps.orders.models import Parcel

class TrackingStatus(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE, related_name='tracking_statuses')
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parcel.tracking_number} - {self.status}"

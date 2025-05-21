from django.db import models
from django.conf import settings

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    subject = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Zgłoszenie #{self.id} - {self.subject}"

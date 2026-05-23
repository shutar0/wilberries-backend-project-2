from django.db import models
from django.conf import settings


class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=255)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.conf import settings # Import settings to reference user model

class Feedback(models.Model):
    # Existing fields ...
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,   # Allows empty values in DB
        blank=True   # Allows empty values in forms
    )
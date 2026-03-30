from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    opening_hours = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
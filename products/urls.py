from django.db import models

class Restaurant(models.Model):

    has_delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name
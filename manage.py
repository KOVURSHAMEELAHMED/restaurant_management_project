from django.db import models

class OrderStatus(models.Model):
    name = models.charField(max_length=50, unique=True)

    def __str__(self):
        return self.name
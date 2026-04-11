from django.db import models

class DeliveryZone(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True
    )
    min_order_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    delivery_fee = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
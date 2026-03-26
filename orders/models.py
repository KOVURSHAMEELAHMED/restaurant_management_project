from django.db import models
from .utils import generate_unique_order_id

class Order(models.Model):
    # Short, user-friendly ID (e.g., XJ8K2L9P)
    order_number = models.CharField(
        max_length=12, 
        unique=True, 
        editable=False, 
        blank=True
    )
    # ... other fields (order_date, etc.) ...

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = generate_unique_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number}"
from django.db import models

class PaymentMethod(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="Name of the payment method (e.g., Credit Card)"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        help_text="Optional explanation of the payment method"
    )
    is_active = models.BooleanField(
        default=True, 
        help_text="Whether this payment method is currently available"
    )

    def __str__(self):
        return self.name
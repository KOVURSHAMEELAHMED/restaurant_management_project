from django.db import models
from django.utils import timezone
# Import other models if needed (e.g., Customer, MenuItem)

class Order(models.Model):
    # Existing fields (adjust to match your actual Order model)
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('preparing', 'Preparing'),
            ('ready', 'Ready'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )
    
    # NEW FIELD: Customer Notes
    customer_notes = models.TextField(
        blank=True,
        null=True,
        help_text="Special instructions, delivery notes, allergy information, or any other customer requests"
    )
    
    # Optional: Timestamps for tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.order_number} - {self.customer_name}"
    
    class Meta:
        ordering = ['-order_date']
        verbose_name_plural = "Orders"
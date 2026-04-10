from django.db import models
from django.utils import timezone

class Order(models.Model):
    # Define status choices as constants
    STATUS_PENDING = 'PENDING'
    STATUS_CONFIRMED = 'CONFIRMED'
    STATUS_PREPARING = 'PREPARING'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_CANCELLED = 'CANCELLED'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_PREPARING, 'Preparing'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    
    # Order fields
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Other fields like items, total_amount, etc.
    # ...
    
    def mark_as_completed(self):
        """
        Mark the order as completed.
        Updates the status to 'COMPLETED' and sets the completed_at timestamp.
        """
        self.status = self.STATUS_COMPLETED
        self.completed_at = timezone.now()
        self.save()
    
    def __str__(self):
        return f"Order {self.order_number} - {self.status}"
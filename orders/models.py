from django.db import models
from django.db.models import Sum

class Order(models.Model):
    # Example status choices
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def calculate_total_revenue(cls):
        """
        Returns the sum of 'total_amount' for all orders with a 'COMPLETED' status.
        """
        # .aggregate() returns a dictionary, e.g., {'total': 150.50}
        result = cls.objects.filter(status='COMPLETED').aggregate(total=Sum('total_amount'))
        return result['total'] or 0.00  # Return 0.00 if no completed orders exist
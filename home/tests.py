from django.db import models

class LoyaltyProgram(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="Name of the loyalty tier (e.g., Silver Member)"
    )
    points_required = models.PositiveIntegerField(
        unique=True, 
        help_text="Minimum points required to reach this tier"
    )
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        help_text="Discount percentage (e.g., 5.00 for 5%)"
    )
    description = models.TextField(
        blank=True, 
        help_text="Brief explanation of the benefits"
    )

    def __str__(self):
        return f"{self.name} ({self.points_required} pts)"
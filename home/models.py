from django.db import models

class LoyaltyProgram(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        help_text="Unique name for the tier (e.g., Bronze, Silver, Gold)"
    )
    points_per_dollar_spent = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=1.00,
        help_text="Points earned for every $1 spent"
    )
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck this to temporarily disable the program"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Loyalty Program"
        verbose_name_plural = "Loyalty Programs"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.points_per_dollar_spent} pts/$)"
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"


class Table(models.Model):
    # Unique table number field
    table_number = models.IntegerField(
        unique=True,
        help_text="Unique number identifying the table (e.g., 1, 2, 3)"
    )
    
    # Capacity field
    capacity = models.IntegerField(
        help_text="Number of people the table can comfortably seat"
    )
    
    # Availability field with default True
    is_available = models.BooleanField(
        default=True,
        help_text="Is the table currently available for reservations?"
    )
    
    def __str__(self):
        """String representation for easy readability in admin interface"""
        status = "Available" if self.is_available else "Reserved"
        return f"Table {self.table_number} (Capacity: {self.capacity}) - {status}"
    
    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"
        ordering = ['table_number']  # Orders tables by their number by default
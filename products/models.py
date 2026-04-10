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
    table_number = models.IntegerField(unique=True, help_text="Unique number identifying the table")
    capacity = models.IntegerField(help_text="Maximum number of people the table can seat")
    is_available = models.BooleanField(default=True, help_text="Is the table currently available?")
    location = models.CharField(max_length=100, help_text="Table location (e.g., Window Side, Patio, Main Dining Room)")
    
    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
    
    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"
        ordering = ['table_number']  # Orders tables by their number by default
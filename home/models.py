from django.db import models

class Table(models.Model):
    TABLE_LOCATIONS = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('patio', 'Patio'),
        ('bar', 'Bar Area'),
        ('private', 'Private Room'),
    ]
    
    TABLE_TYPES = [
        ('standard', 'Standard'),
        ('booth', 'Booth'),
        ('high_top', 'High Top'),
        ('round', 'Round'),
    ]
    
    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField(help_text="Maximum number of guests this table can accommodate")
    is_available = models.BooleanField(default=True, help_text="Is the table currently available?")
    location = models.CharField(max_length=20, choices=TABLE_LOCATIONS, default='indoor')
    table_type = models.CharField(max_length=20, choices=TABLE_TYPES, default='standard')
    is_smoking = models.BooleanField(default=False)
    has_wheelchair_access = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
    
    class Meta:
        ordering = ['table_number']
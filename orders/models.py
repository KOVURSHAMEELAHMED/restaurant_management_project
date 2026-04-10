from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    # Add the capacity field - THIS IS THE NEW FIELD
    capacity = models.IntegerField(
        default=0,
        help_text="Maximum number of guests the restaurant can accommodate",
        verbose_name="Maximum Capacity"
    )
    
    # Optional: Add address and contact fields
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
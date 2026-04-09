from django.db import models

class MenuItem(models.Model):
    # Existing fields (example - adjust to match your actual model)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # e.g., 'Appetizer', 'Main', 'Dessert'
    is_available = models.BooleanField(default=True)
    
    # NEW FIELD: Allergens
    allergens = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Comma-separated list of allergens (e.g., 'gluten, nuts, dairy, eggs')"
    )
    
    def __str__(self):
        # Option 1: Simple display
        return self.name
        
        # Option 2: Include allergen info if present
        # if self.allergens:
        #     return f"{self.name} (Allergens: {self.allergens})"
        # return self.name
    
    class Meta:
        verbose_name_plural = "Menu Items"
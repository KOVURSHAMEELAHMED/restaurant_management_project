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
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
    
    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"
        ordering = ['table_number']


class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    max_capacity = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Cuisine"
        verbose_name_plural = "Cuisines"
        ordering = ['name']


class MenuItem(models.Model):
    # Basic menu item fields
    name = models.CharField(max_length=200, help_text="Name of the dish")
    description = models.TextField(blank=True, null=True, help_text="Description of the dish")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in dollars")
    
    # Foreign key to Cuisine - THIS IS THE NEW FIELD
    cuisine = models.ForeignKey(
        Cuisine, 
        on_delete=models.SET_NULL,  # If cuisine is deleted, set this field to NULL
        null=True,                   # Allows NULL values in the database
        blank=True,                  # Allows the field to be left blank in forms
        related_name='menu_items',   # Allows accessing menu items from cuisine: cuisine.menu_items.all()
        help_text="The cuisine type for this menu item"
    )
    
    # Additional optional fields
    is_vegetarian = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.cuisine:
            return f"{self.name} ({self.cuisine.name}) - ${self.price}"
        return f"{self.name} (No Cuisine) - ${self.price}"
    
    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ['cuisine', 'name']  # Order by cuisine first, then by name
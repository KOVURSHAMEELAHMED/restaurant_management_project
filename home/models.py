from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MenuCategory(models.Model):
    """Category model for organizing menu items"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    display_order = models.IntegerField(default=0, help_text="Order in which categories appear")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Menu Categories"
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """Menu item model for restaurant items"""
    
    # Basic Information
    name = models.CharField(max_length=200, help_text="Name of the menu item")
    description = models.TextField(help_text="Detailed description of the menu item")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Price of the menu item"
    )
    
    # Category relationship
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name='menu_items',
        help_text="Category this item belongs to"
    )
    
    # Optional image field for later image upload functionality
    image = models.ImageField(
        upload_to='menu_images/',
        blank=True,
        null=True,
        help_text="Optional image of the menu item"
    )
    
    # Additional useful fields for a restaurant menu
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    calories = models.IntegerField(blank=True, null=True, help_text="Calories per serving")
    preparation_time = models.IntegerField(blank=True, null=True, help_text="Preparation time in minutes")
    
    # Metadata
    display_order = models.IntegerField(default=0, help_text="Order in which items appear within category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ['category__display_order', 'display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    @property
    def formatted_price(self):
        """Return price formatted as string with 2 decimal places"""
        return f"${self.price:.2f}"
from django.db import models
from django.core.validators import MinValueValidator
# Import your menu model (adjust the name if it's RestaurantMenu)
from menu.models import MenuItem 
from .models import Order

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='items'
    )
    menu_item = models.ForeignKey(
        MenuItem, 
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    price_at_time_of_order = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    def __str__(self):
        return f'{self.quantity} x {self.menu_item.name}'
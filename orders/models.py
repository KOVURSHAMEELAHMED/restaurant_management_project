from django.db import models
from decimal import Decimal

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    # ... other order fields ...

    def calculate_total(self):
        """Iterates through related items and returns the grand total."""
        total = sum(item.get_item_total() for item in self.items.all())
        return Decimal(total)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey('home.MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Price at time of order

    def get_item_total(self):
        return self.price * self.quantity
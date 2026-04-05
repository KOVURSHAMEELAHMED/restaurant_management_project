from django.db import models

class Order(models.Model):
    # ... your existing fields ...

    def get_total_item_count(self):
        """
        Calculates and returns the total number of items in the order.
        """
        # This assumes your OrderItem model has a 'quantity' field 
        # and a related_name of 'items' or 'orderitem_set'
        return sum(item.quantity for item in self.items.all())

from django.db import models

class Order(models.Model):
    # ... existing fields like created_at, customer, etc. ...

    def get_unique_item_names(self) -> list:
        """
        Retrieves a list of unique names for all MenuItems in this order.
        """
        # 1. Access related OrderItems (using the default _set manager)
        # 2. Extract the name from the linked MenuItem
        # 3. Use a set to filter out duplicates automatically
        item_names = {
            item.menu_item.name 
            for item in self.orderitem_set.all()
        }
        
        # Return as a sorted list for consistent output
        return sorted(list(item_names))
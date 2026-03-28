from django.db import models
from .utils import calculate_discount  # Assuming utility is in utils.py

class Order(models.Model):
    # Your existing fields (e.g., date, customer, status)
    
    def calculate_total(self):
        """
        Calculates the total cost of the order by summing up 
        all related items and applying discounts.
        """
        total = 0
        # Accessing related items (assuming a ForeignKey from OrderItem to Order)
        items = self.items.all() 
        
        for item in items:
            # Apply the utility function to the item's base price
            discounted_price = calculate_discount(item.price, item.discount_rate)
            total += discounted_price * item.quantity
            
        return total
from django.db import models

class Order(models.Model):
    # Your existing fields go here (e.g., items, total_price, etc.)
    
    # New field to automatically record creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} created on {self.created_at}"
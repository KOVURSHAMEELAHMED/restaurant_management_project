from django.db import models

class OrderManager(models.Manager):
    def with_status(self, status):
        """
        Returns all orders filtered by a specific status.
        Example: Order.objects.with_status('pending')
        """
        return self.filter(status=status)

class Order(models.Model):
    # Field definitions
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Assign the custom manager
    objects = OrderManager()

    def __str__(self):
        return f"Order {self.id} - {self.status}"
from django.db import models
from django.db.models import Count

class MenuItemManager(models.Manager):
    def get_top_selling_items(self, num_items=5):
        """
        Annotates each item with the count of related order items,
        orders by that count descending, and limits the result.
        """
        return self.get_queryset().annotate(
            total_sales=Count('orderitem')  # 'orderitem' is the default lowercase related name
        ).order_by('-total_sales')[:num_items]

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # ... other fields ...

    # 2. Attach the manager to the model
    objects = MenuItemManager()

    def __str__(self):
        return self.name
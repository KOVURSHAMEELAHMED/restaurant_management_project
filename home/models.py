from django.db import models

# 1. Create the Custom Manager Class
class MenuItemManager(models.Manager):
    def get_budget_items(self, max_price):
        # 2. Define the filtering logic
        return self.filter(price__lt=max_price)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # 3. Attach the custom manager to the model
    objects = MenuItemManager()

    def __str__(self):
        return self.name
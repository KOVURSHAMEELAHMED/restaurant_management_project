from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    # ... other fields ...

    def get_total_menu_items(self):
        """
        Returns the total number of menu items associated with this restaurant.
        """
        return self.menu_items.count()
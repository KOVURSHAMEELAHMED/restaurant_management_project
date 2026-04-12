from django.db import models
from datetime import date

class DailySpecial(models.Model):
    # Links to MenuItem or RestaurantMenu
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        # Ensures a menu item isn't listed twice for the same date
        unique_together = (('menu_item', 'date'),)

    def __str__(self):
        return f"{self.menu_item.name} special on {self.date}"
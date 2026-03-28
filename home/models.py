from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Add this line:
    is_daily_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name
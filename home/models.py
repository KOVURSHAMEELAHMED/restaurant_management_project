from django.db import models

class MenuItem(models.Model):
    # ... existing fields ...
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # ADD THIS LINE
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models

class AvailableItemManager(models.Manager):
    def get_queryset(self):
        # Override to ensure it filters by default, or just use a custom method
        return super().get_queryset().filter(is_available=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    # ... other fields ...

    # Option 1: Using a Custom Manager (Recommended for cleaner code)
    objects = models.Manager() # Default manager
    available = AvailableItemManager() # Custom manager

    def __str__(self):
        return self.name
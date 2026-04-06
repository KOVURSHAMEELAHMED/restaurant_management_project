from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50) # Assuming this field exists
    # ... other fields ...

    @classmethod
    def get_items_by_cuisine(cls, cuisine_type):
        """
        Returns a QuerySet of menu items filtered by the given cuisine_type.
        """
        return cls.objects.filter(cuisine__iexact=cuisine_type)
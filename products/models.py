from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50) # Or models.ForeignKey(Cuisine, ...)
    # ... other fields ...

    @classmethod
    def get_items_by_cuisine(cls, cuisine_type):
        """
        Returns a queryset of menu items matching the specified cuisine type.
        """
        return cls.objects.filter(cuisine__iexact=cuisine_type)
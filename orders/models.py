from django.db import models

class MenuItem(models.Model):
    # ... existing fields ...
    is_vegetarian = models.BooleanField(default=False)
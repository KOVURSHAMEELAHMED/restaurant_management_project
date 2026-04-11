from django.db import models

class MenuItem(models.Model):
    # ... your existing fields (name, price, etc.) ...
    
    is_gluten_free = models.BooleanField(
        default=False, 
        help_text='Indicates if the menu item is gluten-free.'
    )

    def __str__(self):
        return self.name
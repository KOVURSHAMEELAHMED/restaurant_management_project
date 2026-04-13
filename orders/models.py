from django.db import models

class MenuItem(models.Model):
    # ... existing fields (name, price, etc.) ...
    
    is_featured = models.BooleanField(
        default=False, 
        help_text="Mark this item as featured to highlight it on the website or promotions."
    )

    def __str__(self):
        return self.name
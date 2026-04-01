from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_url='menu_items/', blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    # ManyToManyField allows ingredients to be shared among menu items
    ingredients = models.ManyToManyField(Ingredient, related_name='menu_items')

    def __str__(self):
        return self.name
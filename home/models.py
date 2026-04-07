class MenuItem(models.Model):
    # ... existing fields (name, price, etc.) ...
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
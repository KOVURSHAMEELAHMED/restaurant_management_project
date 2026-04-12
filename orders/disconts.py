from django.db import models

class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.percentage * 100}% off)"
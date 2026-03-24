import datetime
from django.db import models

class DailySpecialManager(models.Manager):
    def upcoming(self):
        """
        Returns specials where the date is today or in the future.
        """
        today = datetime.date.today()
        return self.filter(date__gte=today)

class DailySpecial(models.Model):
    # ... your existing fields (e.g., name, price, date) ...
    name = models.CharField(max_length=100)
    date = models.DateField()

    # Attach the custom manager
    objects = DailySpecialManager()

    def __str__(self):
        return f"{self.name} - {self.date}"

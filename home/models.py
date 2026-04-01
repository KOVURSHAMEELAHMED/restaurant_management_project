from django.db import models

class OpeningHour(models.Model):
    WEEKDAYS = [
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),
    ]
    
    day = models.IntegerField(choices=WEEKDAYS, unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField(default=False)  # For holidays or specific closed days

    class Meta:
        ordering = ['day']

    def __str__(self):
        return f"{self.get_day_display()}: {self.opening_time} - {self.closing_time}"
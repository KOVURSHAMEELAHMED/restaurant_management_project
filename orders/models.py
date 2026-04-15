from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    # Add other general fields here as needed
    
    def __str__(self):
        return self.name

class DailyOperatingHours(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    restaurant = models.ForeignKey(
        Restaurant, 
        on_delete=models.CASCADE, 
        related_name='operating_hours'
    )
    day_of_week = models.CharField(
        max_length=10, 
        choices=DAYS_OF_WEEK
    )
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        verbose_name_plural = "Daily Operating Hours"
        # Optional: Ensures a restaurant can't have duplicate entries for the same day
        unique_together = ('restaurant', 'day_of_week')

    def __str__(self):
        return f"{self.restaurant.name} - {self.day_of_week}: {self.opening_time} to {self.closing_time}"
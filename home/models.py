from django.db import models

class Restaurant(models.Model):
    # ... existing fields ...
    opening_hours = models.CharField(
        max_length=100, 
        default="11:00 AM - 11:00 PM (EST)",
        help_text="Format: [Opening Time] - [Closing Time] (Time zone)"
    )

    def __str__(self):
        return self.name
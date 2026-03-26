from django.db import models

class Restaurant(models.Model):
    # ... existing fields (name, location, etc.) ...
    
    # Adding the new field
    opening_days = models.CharField(
        max_length=100, 
        help_text="Enter days separated by commas (e.g., Mon,Tue,Wed)",
        default="Mon,Tue,Wed,Thu,Fri,Sat,Sun"
    )

    def __str__(self):
        return self.name
from django.db import models

class Table(models.Model):
    # ... existing fields (like table_number) ...
    
    max_seats = models.IntegerField(
        default=4,
        help_text="Maximum number of customers for this table."
    )

    def __str__(self):
        return f"Table {self.id} ({self.max_seats} seats)"
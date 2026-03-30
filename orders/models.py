from django.db import models
from datetime import timedelta

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    customer_name = models.CharField(max_length=100)

    @classmethod
    def get_available_slots(cls, start_range, end_range, duration_minutes=60):
        """
        Finds available 1-hour slots for all tables within a specific timeframe.
        """
        available_slots = []
        all_tables = Table.objects.all()
        
        current_time = start_range
        while current_time + timedelta(minutes=duration_minutes) <= end_range:
            slot_end = current_time + timedelta(minutes=duration_minutes)
            
            # Check which tables are NOT reserved during this specific slot
            # A table is busy if an existing reservation starts before our slot ends 
            # AND ends after our slot starts.
            busy_tables = cls.objects.filter(
                start_time__lt=slot_end,
                end_time__gt=current_time
            ).values_list('table_id', flat=True)
            
            free_tables = all_tables.exclude(id__in=busy_tables)
            
            if free_tables.exists():
                available_slots.append({
                    "start": current_time,
                    "end": slot_end,
                    "tables": list(free_tables.values('id', 'number', 'capacity'))
                })
            
            # Move to the next slot (e.g., 30-minute increments)
            current_time += timedelta(minutes=30)
            
        return available_slots
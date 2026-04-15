from datetime import datetime
from django.utils import timezone
from .models import DailyOperatingHours

def is_restaurant_open():
    """
    Determines if the restaurant is currently open based on 
    current day and time against DailyOperatingHours model.
    """
    # 1. Get current day and time
    now = timezone.now()
    # weekday() -> Monday is 0, Sunday is 6. 
    # Adjust if your model uses 1=Monday...7=Sunday
    current_day = now.weekday() 
    current_time = now.time()

    # 2. Query the model for today's hours
    try:
        # Assuming DailyOperatingHours has fields: 'day_of_week', 
        # 'opening_time', 'closing_time'
        hours = DailyOperatingHours.objects.get(day_of_week=current_day)
        
        # 3. Compare current time with opening/closing hours
        if hours.opening_time <= current_time <= hours.closing_time:
            return True
        else:
            return False
            
    except DailyOperatingHours.DoesNotExist:
        # If no hours are defined for today, assume closed
        return False
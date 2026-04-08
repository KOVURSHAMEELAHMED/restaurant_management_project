from datetime import datetime
from .models import DailyOperatingHours

def is_reservation_time_valid(proposed_datetime):
    """
    Validates if a proposed reservation time falls within the restaurant's
    operating hours for that specific day of the week.
    """
    # 1. Get the day of the week (0 = Monday, 6 = Sunday)
    day_index = proposed_datetime.weekday()
    
    # 2. Map index to your model's day format (assuming standard names)
    days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday'
    ]
    target_day = days[day_index]

    try:
        # 3. Look up the operating hours for that day
        hours = DailyOperatingHours.objects.get(day=target_day)
        
        # 4. Check if the proposed time is between opening and closing
        # proposed_datetime.time() extracts only the time part for comparison
        reservation_time = proposed_datetime.time()
        
        if hours.opening_time <= reservation_time <= hours.closing_time:
            return True
            
    except DailyOperatingHours.DoesNotExist:
        # If no hours are defined for that day, assume closed
        return False

    return False
from datetime import datetime, time
import calendar
from typing import Dict, Tuple, Optional

# Restaurant operating hours configuration
# Format: day_of_week: (open_time, close_time)
# Using 24-hour format for easier comparison
RESTAURANT_HOURS = {
    0: (time(9, 0), time(22, 0)),   # Monday: 9:00 AM - 10:00 PM
    1: (time(9, 0), time(22, 0)),   # Tuesday: 9:00 AM - 10:00 PM
    2: (time(9, 0), time(22, 0)),   # Wednesday: 9:00 AM - 10:00 PM
    3: (time(9, 0), time(22, 0)),   # Thursday: 9:00 AM - 10:00 PM
    4: (time(9, 0), time(23, 0)),   # Friday: 9:00 AM - 11:00 PM
    5: (time(10, 0), time(23, 0)),  # Saturday: 10:00 AM - 11:00 PM
    6: (time(10, 0), time(21, 0)),  # Sunday: 10:00 AM - 9:00 PM
}

# Special hours for holidays (optional)
SPECIAL_HOURS = {
    # Format: (month, day): (open_time, close_time, is_closed)
    (12, 25): (None, None, True),   # Christmas Day - Closed
    (1, 1): (None, None, True),     # New Year's Day - Closed
    (7, 4): (time(12, 0), time(18, 0), False),  # July 4th: 12 PM - 6 PM
    (11, 28): (time(11, 0), time(16, 0), False),  # Thanksgiving: 11 AM - 4 PM
}


def is_restaurant_open(check_datetime: Optional[datetime] = None) -> bool:
    """
    Determine if the restaurant is currently open based on operating hours.
    
    Args:
        check_datetime (datetime, optional): The datetime to check. If None, uses current time.
        
    Returns:
        bool: True if restaurant is open, False if closed
        
    Examples:
        >>> is_restaurant_open()  # Check current time
        True
        
        >>> from datetime import datetime
        >>> check_time = datetime(2024, 1, 15, 14, 30)  # Monday 2:30 PM
        >>> is_restaurant_open(check_time)
        True
        
        >>> check_time = datetime(2024, 1, 15, 23, 0)  # Monday 11:00 PM
        >>> is_restaurant_open(check_time)
        False
    """
    # Use current time if no datetime provided
    if check_datetime is None:
        check_datetime = datetime.now()
    
    # Check for special hours/holidays first
    is_special, special_status = check_special_hours(check_datetime)
    if is_special:
        return special_status
    
    # Get the day of week (0 = Monday, 6 = Sunday)
    day_of_week = check_datetime.weekday()
    current_time = check_datetime.time()
    
    # Check if restaurant has defined hours for this day
    if day_of_week not in RESTAURANT_HOURS:
        return False  # Closed if no hours defined
    
    open_time, close_time = RESTAURANT_HOURS[day_of_week]
    
    # Handle closing time that goes past midnight
    if close_time <= open_time:
        # If close time is earlier than open time, assume it's next day
        if current_time >= open_time or current_time <= close_time:
            return True
        return False
    else:
        # Normal hours (same day)
        return open_time <= current_time <= close_time


def check_special_hours(check_datetime: datetime) -> Tuple[bool, bool]:
    """
    Check if the given datetime falls on a special day with modified hours.
    
    Args:
        check_datetime (datetime): The datetime to check
        
    Returns:
        Tuple[bool, bool]: (is_special, is_open)
            - is_special: True if date has special hours defined
            - is_open: True if open, False if closed (only valid if is_special is True)
    """
    month = check_datetime.month
    day = check_datetime.day
    current_time = check_datetime.time()
    
    # Check if date is in special hours
    if (month, day) in SPECIAL_HOURS:
        open_time, close_time, is_closed = SPECIAL_HOURS[(month, day)]
        
        if is_closed:
            return True, False
        
        if open_time and close_time:
            # Check if current time falls within special hours
            return True, (open_time <= current_time <= close_time)
        
        return True, True  # Special day with regular hours
    
    return False, False  # Not a special day


def get_restaurant_status_message() -> str:
    """
    Get a human-readable status message about restaurant hours.
    
    Returns:
        str: Status message like "Open until 10:00 PM" or "Closed. Opens tomorrow at 9:00 AM"
    """
    now = datetime.now()
    is_open = is_restaurant_open(now)
    
    if is_open:
        # Find closing time for today
        day_of_week = now.weekday()
        if day_of_week in RESTAURANT_HOURS:
            _, close_time = RESTAURANT_HOURS[day_of_week]
            close_time_str = close_time.strftime("%I:%M %p").lstrip("0")
            return f"We're open! Closing at {close_time_str}"
        return "We're open!"
    else:
        # Find next opening time
        next_open = get_next_opening_time(now)
        if next_open:
            next_open_str = next_open.strftime("%A at %I:%M %p").lstrip("0")
            return f"We're closed. Next opening: {next_open_str}"
        return "We're currently closed"


def get_next_opening_time(from_datetime: Optional[datetime] = None) -> Optional[datetime]:
    """
    Get the next datetime when the restaurant will be open.
    
    Args:
        from_datetime (datetime, optional): Starting datetime. If None, uses current time.
        
    Returns:
        Optional[datetime]: Next opening time, or None if no future opening found
    """
    if from_datetime is None:
        from_datetime = datetime.now()
    
    # Check up to 7 days ahead
    for days_ahead in range(1, 8):
        check_date = from_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        check_date = check_date + timedelta(days=days_ahead)
        day_of_week = check_date.weekday()
        
        if day_of_week in RESTAURANT_HOURS:
            open_time, _ = RESTAURANT_HOURS[day_of_week]
            opening_datetime = datetime.combine(check_date.date(), open_time)
            
            # If checking for today, only return if opening time is in the future
            if days_ahead == 1 and opening_datetime <= from_datetime:
                continue
                
            return opening_datetime
    
    return None


# Alternative version with more flexible configuration
class RestaurantHours:
    """
    A class-based approach for managing restaurant hours with more flexibility.
    """
    
    def __init__(self, hours_config: Dict[int, Tuple[time, time]] = None):
        """
        Initialize restaurant hours with custom configuration.
        
        Args:
            hours_config: Dictionary mapping day of week to (open_time, close_time)
        """
        self.hours_config = hours_config or RESTAURANT_HOURS.copy()
    
    def is_open(self, check_datetime: Optional[datetime] = None) -> bool:
        """Check if restaurant is open at the given time."""
        if check_datetime is None:
            check_datetime = datetime.now()
        
        day_of_week = check_datetime.weekday()
        current_time = check_datetime.time()
        
        if day_of_week not in self.hours_config:
            return False
        
        open_time, close_time = self.hours_config[day_of_week]
        
        # Handle overnight hours
        if close_time <= open_time:
            return current_time >= open_time or current_time <= close_time
        else:
            return open_time <= current_time <= close_time
    
    def get_hours_for_day(self, day_of_week: int) -> Optional[Tuple[time, time]]:
        """Get opening hours for a specific day."""
        return self.hours_config.get(day_of_week)
    
    def is_closed_all_day(self, check_datetime: datetime) -> bool:
        """Check if restaurant is closed for the entire day."""
        day_of_week = check_datetime.weekday()
        return day_of_week not in self.hours_config


# Simple version (as requested in the task)
def is_restaurant_open_simple() -> bool:
    """
    Simple version of the function with hardcoded hours.
    Monday-Friday: 9:00 AM to 10:00 PM
    Saturday-Sunday: 10:00 AM to 9:00 PM
    """
    now = datetime.now()
    current_day = now.weekday()  # 0=Monday, 6=Sunday
    current_time = now.time()
    
    # Monday to Friday (0-4)
    if current_day < 5:  # Monday to Friday
        open_time = time(9, 0)   # 9:00 AM
        close_time = time(22, 0)  # 10:00 PM
        return open_time <= current_time <= close_time
    
    # Saturday (5) and Sunday (6)
    else:
        open_time = time(10, 0)  # 10:00 AM
        close_time = time(21, 0)  # 9:00 PM
        return open_time <= current_time <= close_time
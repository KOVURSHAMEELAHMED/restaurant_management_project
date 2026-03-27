from datetime import datetime

def format_datetime(dt):
    """
    Formats a datetime object into a user-friendly string.
    Example: 'January 1, 2023 at 10:30 AM'
    """
    if dt is None:
        return ""
    
    # %B = Month, %d = Day, %Y = Year, %I = 12-hr Hour, %M = Minute, %p = AM/PM
    return dt.strftime("%B %d, %Y at %I:%M %p")

# Example usage:
# now = datetime(2023, 1, 1, 10, 30)
# print(format_datetime(now))  # Output: January 01, 2023 at 10:30 AM
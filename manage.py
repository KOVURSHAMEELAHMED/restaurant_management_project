from datetime import datetime
from django.utils import timezone
from .models import DailyOperatingHours

def get_today_operating_hours():
    """
    Returns the (open_time, close_time) for the current day.
    Useful for hotel dashboards and guest-facing digital menus.
    """


    current_day = timezone.now().strftime('%A')

    try:

        hours_record = DailyOperatingHours.objects.get(day=current_day)

        return (hours_record.open_time, hours_record.close_time)

    except DailyOperatingHours.DoesNotExist:

        return (None, None)
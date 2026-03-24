from django.db.models import Sum
from .models import Order

def get_daily_sales_total(date):
    """
    Calculates the total revenue for a specific date.
    """
    # Filter orders by the date part of the created_at DateTimeField
    daily_orders = Order.objects.filter(created_at__date=date)
    
    # Aggregate the sum of total_price
    result = daily_orders.aggregate(total_sum=Sum('total_price'))
    
    # Return the sum, or 0.00 if no orders exist (result['total_sum'] would be None)
    return result['total_sum'] or 0
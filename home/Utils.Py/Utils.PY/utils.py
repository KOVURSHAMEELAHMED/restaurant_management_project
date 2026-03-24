from decimal import Decimal, ROUND_HALF_UP

def calculate_tip_amount(order_total, tip_percentage):
    """
    Calculates the tip amount based on the order total and a tip percentage.

    Args:
        order_total (Decimal/float): The total cost of the order.
        tip_percentage (int): The percentage to tip (e.g., 15 for 15%).

    Returns:
        Decimal: The calculated tip amount rounded to two decimal places.
    """
    # Convert inputs to Decimal for financial precision
    total = Decimal(str(order_total))
    percentage = Decimal(str(tip_percentage))
    
    tip_amount = total * (percentage / 100)
    
    # Round to 2 decimal places
    return tip_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
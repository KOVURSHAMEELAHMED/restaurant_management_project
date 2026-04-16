from decimal import Decimal, ROUND_HALF_UP

def calculate_sales_tax(amount: Decimal, tax_rate: Decimal) -> Decimal:
    """
    Calculates the sales tax for a given amount and tax rate.
    
    Args:
        amount: A Decimal value representing the subtotal before tax.
        tax_rate: A Decimal value representing the tax rate (e.g., 0.05 for 5%).
        
    Returns:
        The calculated sales tax amount as a Decimal, rounded to 2 decimal places.
    """
    # Calculate initial tax amount
    tax_amount = amount * tax_rate
    
    # Use quantize to ensure result is rounded to exactly two decimal places
    # ROUND_HALF_UP ensures standard financial rounding (e.g., 0.005 becomes 0.01)
    return tax_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
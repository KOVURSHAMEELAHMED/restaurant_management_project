from decimal import Decimal

def calculate_order_total(order_items):
    """
    Calculates the total cost for a list of order items.
    
    Args:
        order_items (list): A list of dictionaries or objects. 
        Each must have 'price' and 'quantity' keys/attributes.
        
    Returns:
        Decimal: The total sum of (price * quantity).
    """
    # Handle empty lists or None values gracefully
    if not order_items:
        return Decimal('0.00')

    total = sum(
        (Decimal(str(item.get('price', 0))) * item.get('quantity', 0))
        for item in order_items
    )
    
    # Quantize to 2 decimal places for currency consistency
    return total.quanti                                 

Example Usage

items = [
    {'price': 12.50, 'quantity': 2},
    {'price': 5.00, 'quantity': 1}
]

print(calculate_order_total(items))  # Output: 30.00ze(Decimal('0.01'))
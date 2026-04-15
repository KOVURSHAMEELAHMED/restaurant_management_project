def calculate_estimated_prep_time(order_items):
    """
    Calculates the total estimated prep time in minutes based on items.
    
    Args:
        order_items (list): List of dictionaries, each with 'quantity' 
                            and 'prep_time_minutes'.
    Returns:
        int: Total prep time in minutes.
    """
    total_prep_time = 0
    
    for item in order_items:
        # Multiply item prep time by quantity and add to total
        total_prep_time += item.get('prep_time_minutes', 0) * item.get('quantity', 0)
        
    return int(total_prep_time)

# Example Usage:
# items = [
#     {'menu_item_id': 1, 'quantity': 2, 'prep_time_minutes': 10}, # 20 mins
#     {'menu_item_id': 5, 'quantity': 1, 'prep_time_minutes': 15}  # 15 mins
# ]
# total = calculate_estimated_prep_time(items) # Returns 35
from django.db.models import Q
from .models import Table  # Assuming you have a Table model

def get_available_tables_by_capacity(num_guests):
    """
    Filter available tables based on required capacity.
    
    Args:
        num_guests (int): The number of guests to accommodate
        
    Returns:
        QuerySet: A Django QuerySet containing Table objects that are available
                 and have capacity >= num_guests
        
    Example:
        >>> available_tables = get_available_tables_by_capacity(4)
        >>> for table in available_tables:
        ...     print(f"Table {table.table_number}: Capacity {table.capacity}")
    """
    # Validate input
    if not isinstance(num_guests, int) or num_guests <= 0:
        return Table.objects.none()  # Return empty queryset for invalid input
    
    # Query for available tables with sufficient capacity
    available_tables = Table.objects.filter(
        is_available=True,
        capacity__gte=num_guests  # gte = greater than or equal to
    ).order_by('capacity', 'table_number')  # Order by capacity then table number
    
    return available_tables


# Optional: Add additional utility functions for more complex scenarios
def get_available_tables_by_capacity_and_preferences(num_guests, **preferences):
    """
    Extended function that filters tables based on capacity and additional preferences.
    
    Args:
        num_guests (int): The number of guests to accommodate
        **preferences: Additional filters like location, table_type, etc.
        
    Returns:
        QuerySet: Filtered Table objects matching all criteria
    """
    if not isinstance(num_guests, int) or num_guests <= 0:
        return Table.objects.none()
    
    # Start with base query
    query = Table.objects.filter(
        is_available=True,
        capacity__gte=num_guests
    )
    
    # Apply additional filters if provided
    if preferences:
        query = query.filter(**preferences)
    
    return query.order_by('capacity', 'table_number')


def get_best_available_table(num_guests):
    """
    Find the best available table for the given number of guests.
    Returns the table with minimum excess capacity (most efficient fit).
    
    Args:
        num_guests (int): The number of guests to accommodate
        
    Returns:
        Table or None: The best matching table or None if no table available
    """
    available_tables = get_available_tables_by_capacity(num_guests)
    
    if not available_tables.exists():
        return None
    
    # Find the table with the smallest capacity that still meets the requirement
    # This is the most efficient use of table space
    best_table = available_tables.order_by('capacity').first()
    
    return best_table
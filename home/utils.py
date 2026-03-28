from .models import MenuItem, Cuisine

def get_distinct_cuisines():
    """
    Retrieves a list of all unique cuisine names associated with 
    the current menu items.
    """
    # Use values_list with flat=True to get a simple list of strings
    # distinct() ensures no duplicates are returned
    cuisines = MenuItem.objects.values_list('cuisine__name', flat=True).distinct()
    
    # Convert the QuerySet to a standard Python list
    return list(cuisines)
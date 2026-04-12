def format_currency(amount):
    """
    Takes a numeric value and returns it as a formatted currency string.
    Example: 12.5 -> "$12.50"
    """
    return f"${amount:.2f}"
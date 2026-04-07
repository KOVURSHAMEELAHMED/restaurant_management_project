def calculate_discount(price, discount_percentage):
    """
    Calculates the final price after applying a percentage discount.
    """
    try:
        # Convert inputs to float to handle strings or different numeric types
        price = float(price)
        discount_percentage = float(discount_percentage)

        # Basic validation for realistic values
        if price < 0 or discount_percentage < 0:
            raise ValueError("Price and discount must be non-negative.")
        
        if discount_percentage > 100:
            return 0.0  # Or handle as an error depending on business logic

        discount_amount = (price * discount_percentage) / 100
        final_price = price - discount_amount
        
        return round(final_price, 2)

    except (ValueError, TypeError):
        # Returns None or raises a custom error if inputs aren't numbers
        return None 
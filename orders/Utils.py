import secrets
import string

def generate_unique_order_id(length=8):
    """Generates a unique, short alphanumeric ID for an Order."""
    from .models import Order  # Local import to avoid circular dependency
    
    # Character set: Uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    
    while True:
        # Generate a random string
        new_id = ''.join(secrets.choice(characters) for _ in range(length))
        
        # Check if this ID already exists in the database
        if not Order.objects.filter(order_number=new_id).exists():
            return new_id
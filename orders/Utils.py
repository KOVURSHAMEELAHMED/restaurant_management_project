import string
import random
from django.apps import apps

def generate_reservation_confirmation_number(length=8):
    """
    Generates a unique, alphanumeric confirmation number.
    """
    # Characters to choose from (Uppercase letters and digits)
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(characters, k=length))
    
    # Import model dynamically to avoid circular imports
    Reservation = apps.get_model('home', 'Reservation')
    
    # Ensure uniqueness in the database
    if Reservation.objects.filter(confirmation_number=code).exists():
        return generate_reservation_confirmation_number(length)
        
    return code
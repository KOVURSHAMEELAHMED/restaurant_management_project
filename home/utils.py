from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_valid_email(email):
    """
    Validates an email address.
    Returns True if valid, False otherwise.
    """
    if not email:
        return False
        
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# re module 
import re

def is_valid_email(email):
    """
    Validates email format using a regular expression.
    """
    if not email:
        return False
        
    # Standard email regex pattern
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    return False
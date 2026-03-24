import logging
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Set up logging to capture unexpected errors
logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
    Validates an email address using Django's built-in validator.
    Returns True if valid, False if invalid or upon error.
    """
    if not email or not isinstance(email, str):
        return False
        
    try:
        # Django's built-in function raises a ValidationError if invalid
        validate_email(email)
        return True
    except ValidationError:
        # Standard invalid format (e.g., missing @ or domain)
        return False
    except Exception as e:
        # Handle and log potential unexpected exceptions to avoid crashes
        logger.error(f"Unexpected error validating email '{email}': {e}")
        return False
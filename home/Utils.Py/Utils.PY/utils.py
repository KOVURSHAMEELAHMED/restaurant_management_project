import re

def validate_phone_number(phone_string):
    """
    Validates a phone number string.
    Matches: +1 123-456-7890, 1234567890, +11234567890, etc.
    """
    # Regex breakdown:
    # ^\+?1?      -> Optional plus and optional country code '1'
    # \s?         -> Optional space
    # \d{3}       -> 3 digits (area code)
    # [\s.-]?     -> Optional separator (space, dot, or hyphen)
    # \d{3}       -> 3 digits
    # [\s.-]?     -> Optional separator
    # \d{4}$      -> 4 digits at the end
    
    pattern = r'^\+?1?\s?\d{3}[\s.-]?\d{3}[\s.-]?\d{4}$'
    
    if re.match(pattern, phone_string):
        return True
    return False
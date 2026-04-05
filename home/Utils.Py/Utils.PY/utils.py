import re

def format_phone_number(phone_str):
    """
    Cleans a string and formats it as (XXX) XXX-XXXX.
    Returns the original string if it doesn't contain exactly 10 digits.
    """
    try:
        # Step 3: Remove all non-numeric characters
        numeric_filter = re.compile(r'[^\d]')
        clean_number = numeric_filter.sub('', str(phone_str))

        # Step 2: Format if we have a standard 10-digit number
        if len(clean_number) == 10:
            return f"({clean_number[:3]}) {clean_number[3:6]}-{clean_number[6:]}"
        
        # Return as-is if it's an extension or international (handle gracefully)
        return phone_str

    except (ValueError, TypeError):
        # Step 3: Handle invalid inputs (like None or non-string objects)
        return ""
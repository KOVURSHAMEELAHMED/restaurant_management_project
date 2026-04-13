from django.db import models

class CustomerProfile(models.Model):
    # ... existing fields (first_name, last_name, etc.) ...

    def get_full_name(self):
        """
        Returns the combined first and last name, 
        handling empty or None values gracefully.
        """
        # Filter out None or empty strings, then join with a space
        parts = [self.first_name, self.last_name]
        full_name = " ".join(filter(None, parts))
        
        return full_name.strip() or "Unnamed User"

    def __str__(self):
        return self.get_full_name()
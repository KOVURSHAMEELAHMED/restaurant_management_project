from django.db import models

class DailySpecial(models.Model):
    # ... (your existing fields like name, price, description) ...

    @staticmethod
    def get_random_special():
        """
        Queries the database for all DailySpecial objects and returns one at random.
        Returns None if no specials exist.
        """
        # .order_by('?') tells the database to return results in a random order.
        # .first() safely returns the first item or None if the queryset is empty.
        return DailySpecial.objects.order_by('?').first()
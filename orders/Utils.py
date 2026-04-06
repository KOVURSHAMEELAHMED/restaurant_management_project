from django.db.models import Avg

def calculate_average_rating(reviews_queryset):
    """
    Calculates the average rating from a QuerySet of reviews.
    Returns 0.0 if the QuerySet is empty.
    """
    # 1. Handle cases with no reviews (Requirement 2)
    count = reviews_queryset.count()
    if count == 0:
        return 0.0

    try:
        # 2 & 3. Sum up ratings and calculate average (Requirement 3)
        # Using a loop as requested, though aggregate() is faster for large sets
        total_sum = sum(review.rating for review in reviews_queryset)
        average = total_sum / count
        
        return float(average)

    except (TypeError, ZeroDivisionError, AttributeError):
        # 4. Graceful error handling (Requirement 4)
        return 0.0
from orders.models import Review
from orders.utils import calculate_average_rating

# Test with reviews
all_reviews = Review.objects.all()
print(f"Average: {calculate_average_rating(all_reviews)}")

# Test with an empty filter
no_reviews = Review.objects.filter(id=0)
print(f"Empty Average: {calculate_average_rating(no_reviews)}")
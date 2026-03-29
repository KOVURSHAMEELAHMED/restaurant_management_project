from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Import MenuItem from its respective location, e.g., from .models import MenuItem

class UserReview(models.Model):
    # Foreign keys to link the review to a user and a specific menu item
    user = models.ForeignKey(User, on_of_delete=models.CASCADE, related_name='reviews')
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, related_name='reviews')
    
    # Rating field restricted between 1 and 5
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Enter a rating between 1 and 5"
    )
    
    comment = models.TextField()
    
    # Automatically record the date/time the review was written
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent a user from reviewing the same item multiple times
        unique_together = ('user', 'menu_item')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.menu_item.name} ({self.rating}★)"
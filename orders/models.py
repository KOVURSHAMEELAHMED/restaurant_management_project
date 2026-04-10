from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define cuisine choices as a tuple of tuples for reusability
CUISINE_CHOICES = (
    ('italian', 'Italian'),
    ('mexican', 'Mexican'),
    ('asian', 'Asian'),
    ('indian', 'Indian'),
    ('chinese', 'Chinese'),
    ('japanese', 'Japanese'),
    ('thai', 'Thai'),
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
    ('mediterranean', 'Mediterranean'),
    ('american', 'American'),
    ('french', 'French'),
    ('other', 'Other'),
)

class UserProfile(models.Model):
    # One-to-one link to Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Preferred cuisine field with choices
    preferred_cuisine = models.CharField(
        max_length=50, 
        choices=CUISINE_CHOICES,
        default='other',
        help_text="Select your favorite type of cuisine"
    )
    
    # You can add more fields here in the future
    # phone_number = models.CharField(max_length=15, blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    # address = models.TextField(blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Timestamps (optional but helpful)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

# Signal to automatically create/update UserProfile when User is created/updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile for every new user"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the UserProfile whenever the User is saved"""
    instance.profile.save()
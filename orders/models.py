from django.db import models

class NewsletterSubscription(models.Model):
    # EmailField ensures valid email format, unique=True prevents duplicates
    email = models.EmailField(unique=True, max_length=255)
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Optional: Track time

    def __str__(self):
        return self.email
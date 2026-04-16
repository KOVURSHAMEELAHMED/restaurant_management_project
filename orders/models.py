from django.db import models

class Staff(models.Model):
    ROLE_CHOICES = [
        ('Chef', 'Chef'),
        ('Waiter', 'Waiter'),
        ('Manager', 'Manager'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order

@receiver(post_save, sender=Order)
def notify_admin_on_order_update(sender, instance, created, **kwargs):
    # We only want to notify on updates, not when the order is first created
    if not created:
        subject = f"Update: Order #{instance.id} Status Changed"
        message = f"The status for Order #{instance.id} has been updated to: {instance.status}."
        admin_email = 'admin@restaurant.com'
        
        send_mail(
            subject,
            message,
            None, # Uses DEFAULT_FROM_EMAIL
            [admin_email],
            fail_silently=False,
        )
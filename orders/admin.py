
from django.contrib import admin, messages
from .models import Order

@admin.action(description="Mark selected orders as Processed")
def mark_orders_processed(modeladmin, request, queryset):
    """
    Updates the status of selected orders to 'Processed'.
    """
    # Bulk update for efficiency
    updated_count = queryset.update(status='Processed')
    
    # Provide feedback to the admin user
    modeladmin.message_user(
        request, 
        f"Successfully marked {updated_count} orders as processed.",
        messages.SUCCESS
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # List the fields you want to see in the admin table
    list_display = ['id', 'customer', 'status', 'created_at']
    
    # Register the custom action here
    actions = [mark_orders_processed]

from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Customize the columns shown in the list view
    list_display = ('id', 'customer', 'total_amount', 'order_status', 'created_at')
    
    # Optional: Make specific fields clickable to edit
    list_display_links = ('id', 'customer')
    
    # Optional: Add filters for quick searching
    list_filter = ('order_status', 'created_at')
    
    # Optional: Enable quick editing of status directly in list
    list_editable = ('order_status',)
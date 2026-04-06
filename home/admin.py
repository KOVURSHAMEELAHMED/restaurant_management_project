from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    # Displays the toggle in the list view
    list_display = ('code', 'discount', 'is_active') 
    
    # Allows you to toggle it without clicking into the coupon details
    list_editable = ('is_active',) 
    
    # Adds a sidebar filter for quick management
    list_filter = ('is_active',)
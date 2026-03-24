from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # 1. Columns to display in the list view
    list_display = ('name', 'address', 'phone_number', 'email', 'is_active')
    
    # 2. Add a search bar for specific fields
    search_fields = ('name', 'address')
    
    # 3. Sidebar filter for boolean or categorical fields
    # (Assuming 'is_active' exists in your Restaurant model)
    list_filter = ('is_active',)

    # Optional: Make the list ordered by name by default
    ordering = ('name',)
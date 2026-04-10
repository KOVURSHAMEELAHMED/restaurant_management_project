from django.contrib import admin
from .models import Restaurant, Table, Cuisine

# Register Restaurant model
admin.site.register(Restaurant)

# Register Table model with custom admin
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'capacity')
    search_fields = ('table_number',)

# Register Cuisine model with custom admin
@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('name',)
    
    # For enhanced version with more fields
    # list_display = ('id', 'name', 'is_active', 'created_at')
    # list_filter = ('is_active', 'created_at')
    # list_editable = ('is_active',)
    
    fields = ('name',)  # For basic version
    # fields = ('name', 'description', 'is_active')  # For enhanced version
from django.contrib import admin
from .models import Restaurant, Table

# Simple registration
admin.site.register(Restaurant)
admin.site.register(Table)

# OR with custom admin interface for better management (Recommended)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available', 'location')
    list_display_links = ('table_number',)
    list_editable = ('is_available',)  # Allow editing availability directly from list view
    list_filter = ('is_available', 'location', 'capacity')
    search_fields = ('table_number', 'location')
    list_per_page = 25
    fields = ('table_number', 'capacity', 'location', 'is_available')
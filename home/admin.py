from django.contrib import admin
from .models import Restaurant, Table

# Register Restaurant model
admin.site.register(Restaurant)

# Register Table model with custom admin interface
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available')
    list_display_links = ('table_number',)
    list_editable = ('is_available',)  # Allows editing availability directly from list view
    list_filter = ('is_available', 'capacity')
    search_fields = ('table_number',)
    list_per_page = 25
    ordering = ('table_number',)
    
    # Add helpful fields for adding/editing
    fields = ('table_number', 'capacity', 'is_available')
    
    # Add a help text for each field
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['table_number'].help_text = "Unique number for this table (e.g., 1, 2, 3)"
        form.base_fields['capacity'].help_text = "Maximum number of people this table can seat"
        form.base_fields['is_available'].help_text = "Check if table is currently available for reservations"
        return form
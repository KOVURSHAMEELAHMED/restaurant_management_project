from django.contrib import admin
from .models import Table

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available', 'location')
    list_filter = ('is_available', 'location')
    search_fields = ('table_number', 'location')
    list_editable = ('is_available', 'capacity')
    list_per_page = 20
    ordering = ('table_number',)
    
    fieldsets = (
        ('Table Information', {
            'fields': ('table_number', 'capacity', 'location')
        }),
        ('Status', {
            'fields': ('is_available',)
        }),
    )

# Register the model with the custom admin class
admin.site.register(Table, TableAdmin)
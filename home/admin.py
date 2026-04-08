from django.contrib import admin
from .models import Table  # Importing your Table model

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available') # Optional: helps you see details at a glance
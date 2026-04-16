from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'contact_email')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'contact_email')
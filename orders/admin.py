from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'order_date', 'status', 'total_amount', 'has_notes')
    list_filter = ('status', 'order_date')
    search_fields = ('order_number', 'customer_name', 'customer_email', 'customer_phone', 'customer_notes')
    list_editable = ('status',)
    readonly_fields = ('order_number', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'customer_name', 'customer_email', 'customer_phone')
        }),
        ('Order Details', {
            'fields': ('total_amount', 'status')
        }),
        ('Customer Notes', {
            'fields': ('customer_notes',),
            'classes': ('wide',),
            'description': 'Any special instructions, delivery notes, or allergy information from the customer'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_notes(self, obj):
        return bool(obj.customer_notes)
    has_notes.boolean = True
    has_notes.short_description = 'Has Notes'

admin.site.register(Order, OrderAdmin)
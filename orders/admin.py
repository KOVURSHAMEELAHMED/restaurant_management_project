from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_available', 'allergens')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description', 'allergens')
    list_editable = ('price', 'is_available')
    
    # If using ManyToManyField with Allergen model:
    # filter_horizontal = ('allergens',)

admin.site.register(MenuItem, MenuItemAdmin)
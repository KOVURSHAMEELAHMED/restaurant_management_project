from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    # Add the custom action name to the actions list
    actions = ['make_unavailable']

    @admin.action(description="Mark selected items as unavailable")
    def make_unavailable(self, request, queryset):
        """
        Updates the is_available field to False for all selected items.
        """
        updated_count = queryset.update(is_available=False)
        
        # Optional: Send a success message to the admin interface
        self.message_user(
            request, 
            f"Successfully marked {updated_count} items as unavailable."
        )
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Inline admin for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend UserAdmin to include profile fields
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_preferred_cuisine', 'is_staff')
    
    def get_preferred_cuisine(self, obj):
        return obj.profile.preferred_cuisine
    get_preferred_cuisine.short_description = 'Preferred Cuisine'

# Register the custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Or simply register UserProfile alone
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_cuisine', 'created_at')
    list_filter = ('preferred_cuisine',)
    search_fields = ('user__username', 'user__email', 'preferred_cuisine')
    raw_id_fields = ('user',)
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  # This will automatically include the new allergens field
        # OR explicitly list fields:
        # fields = ['id', 'name', 'description', 'price', 'category', 'is_available', 'allergens']
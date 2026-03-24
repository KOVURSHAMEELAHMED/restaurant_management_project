from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
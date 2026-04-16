from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # Add 'is_vegetarian' to the tuple below
        fields = ['id', 'name', 'price', 'is_vegetarian'] 
        # Or use fields = '__all__' to include all fields automatically
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    # This displays the category's __str__ representation instead of just an ID
    category = serializers.StringRelatedField() 

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category']
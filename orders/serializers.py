from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class __all__:
        model = MenuItem
        fields = '__all__' # Or list specific fields like ['id', 'name', 'price', 'description']
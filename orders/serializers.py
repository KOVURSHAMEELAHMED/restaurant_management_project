from rest_framework import serializers
from .models import MenuItem

class MenuItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # Including all requested fields
        fields =
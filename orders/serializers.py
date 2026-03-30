from rest_framework import serializers
from .models import MenuItem

class MenuItemAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['is_available']

from rest_framework import serializers
from .models import Cuisine

class CuisineSerializer(serializers.ModelSerializer):
    """Serializer for Cuisine model to convert to/from JSON"""
    
    class Meta:
        model = Cuisine
        fields = ['id', 'name']  # Include both id and name fields
        # Or use: fields = '__all__' to include all fields
        # Or exclude: exclude = ['created_at']
from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'  # Includes all fields from the Table model
        # OR specify fields explicitly:
        # fields = ['id', 'table_number', 'capacity', 'is_available', 'location']
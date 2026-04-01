from rest_framework import serializers
from .models import Order

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['short_id', 'status', 'created_at']
from rest_framework import serializers
from .models import OrderItem

class OrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity']
        extra_kwargs = {'id': {'read_only': True}}

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value
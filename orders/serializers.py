from rest_framework import serializers
from .models import Order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

    def validate_status(self, value):
        # Optional: Add custom logic (e.g., can't move from 'Completed' to 'Pending')
        valid_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid status selection.")
        return value
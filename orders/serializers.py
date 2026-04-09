from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # This will automatically include customer_notes
        # OR explicitly list fields:
        # fields = ['id', 'order_number', 'customer_name', 'customer_email', 
        #          'customer_phone', 'order_date', 'total_amount', 'status', 
        #          'customer_notes', 'created_at', 'updated_at']
        read_only_fields = ['order_number', 'created_at', 'updated_at']
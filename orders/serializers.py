from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity', 'price']

class OrderHistorySerializer(serializers.ModelSerializer):
    # Using the method we created earlier for the count
    item_count = serializers.IntegerField(source='get_total_item_count', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'date_ordered', 'status', 'total_amount', 'item_count', 'items']
from rest_framework import generics
from .models import OrderItem
from .serializers import OrderItemUpdateSerializer
from rest_framework.response import Response
from rest_framework import status

class UpdateOrderItemQuantityView(generics.UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemUpdateSerializer

    def perform_update(self, serializer):
        new_quantity = serializer.validated_data.get('quantity')
        
        if new_quantity == 0:
            # Delete item if quantity is 0
            serializer.instance.delete()
        else:
            # Update quantity
            serializer.save()
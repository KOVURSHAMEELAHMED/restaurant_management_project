from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderStatusSerializer

class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    
    # We use 'patch' because we are only updating one field
    def patch(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderStatusUpdateSerializer

class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated] 
    # Use [permissions.IsAdminUser] if only staff should change status
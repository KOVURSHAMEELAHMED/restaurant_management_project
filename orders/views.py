from rest_framework import generics
from .models import Order
from .serializers import OrderStatusSerializer

class OrderStatusView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    lookup_field = 'short_id'  # This tells DRF to use short_id in the URL
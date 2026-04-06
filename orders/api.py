from rest_framework import generics
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSummarySerializer

class OrderSummaryDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSummarySerializer
    lookup_field = 'id'  # Matches the variable name in your URL path
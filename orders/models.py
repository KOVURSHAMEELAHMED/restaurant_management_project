from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk' # This maps to the ID in the URL
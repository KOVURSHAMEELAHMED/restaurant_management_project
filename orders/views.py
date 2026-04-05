from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderHistorySerializer

class UserOrderHistoryView(generics.ListAPIView):
    serializer_class = OrderHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return orders belonging to the logged-in user
        return Order.objects.filter(user=self.request.user).order_by('-date_ordered')
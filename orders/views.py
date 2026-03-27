from rest_framework.generics import ListAPIView
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer

class PaymentMethodListView(ListAPIView):
    """
    Returns a list of all active payment methods.
    """
    serializer_class = PaymentMethodSerializer
    
    def get_queryset(self):
        return PaymentMethod.objects.filter(is_active=True)
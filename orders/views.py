from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPriceRangeView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        try:
            if min_price:
                queryset = queryset.filter(price__gte=float(min_price))
            if max_price:
                queryset = queryset.filter(price__lte=float(max_price))
        except ValueError:
            # Gracefully handle non-numeric inputs
            raise ValidationError("Price parameters must be valid numbers.")

        return queryset
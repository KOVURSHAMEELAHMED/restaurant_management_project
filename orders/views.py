from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class AvailableMenuItemsView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        # Step 3: Return only items where is_available is True
        return MenuItem.objects.filter(is_available=True)
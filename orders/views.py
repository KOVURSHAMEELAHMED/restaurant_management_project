from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class FeaturedMenuItemsAPIView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        """
        This view returns a list of all menu items
        marked as featured.
        """
        return MenuItem.objects.filter(is_featured=True)
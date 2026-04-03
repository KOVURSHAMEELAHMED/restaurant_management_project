from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemDetailSerializer

class MenuItemDetailView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemDetailSerializer
    # DRF automatically handles the 404 "Not Found" if the ID doesn't exist
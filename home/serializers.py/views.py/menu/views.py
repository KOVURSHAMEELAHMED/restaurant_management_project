from rest_framework import viewsets, permissions
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    # Restrict update/delete to Admin users, allow others to Read
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
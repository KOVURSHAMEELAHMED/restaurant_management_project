from rest_framework import viewsets
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default CRUD actions for MenuCategory.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
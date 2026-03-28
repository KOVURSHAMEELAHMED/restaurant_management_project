from rest_framework import viewsets
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
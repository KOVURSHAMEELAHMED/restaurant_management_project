
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10  # Adjust based on your needs
    page_size_query_param = 'page_size'
    max_page_size = 100

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = MenuItemPagination
    
    # Configure the SearchFilter
    filter_backends = [filters.SearchFilter]
    # This uses __icontains under the hood for case-insensitive partial matches
    search_fields = ['name']
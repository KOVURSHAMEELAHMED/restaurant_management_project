from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSearchSerializer

class MenuItemSearchView(generics.ListAPIView):
    serializer_class = MenuItemSearchSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        query = self.request.query_params.get('q')
        
        if query:
            # Case-insensitive search on the 'name' field
            queryset = queryset.filter(name__icontains=query)
            
        return queryset
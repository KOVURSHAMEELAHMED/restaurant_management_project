from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class DailySpecialsListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        # Filtering ORM for only specials
        return MenuItem.objects.filter(is_daily_special=True)
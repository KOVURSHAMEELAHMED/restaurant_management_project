from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem

class MenuItemCountView(APIView):
    """
    Returns the total count of currently available menu items.
    """
    def get(self, request):
        # Filter for active items and count them
        count = MenuItem.objects.filter(is_available=True).count()
        
        return Response({'total_menu_items': count})
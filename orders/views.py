from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer

@api_view(['GET'])
def get_restaurant_info(request):
    # Grabs the first restaurant entry in the DB
    restaurant = Restaurant.objects.first()
    
    if not restaurant:
        return Response({"error": "Restaurant information not found"}, status=404)
        
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)
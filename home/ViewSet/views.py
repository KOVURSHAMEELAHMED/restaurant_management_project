from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant

class RestaurantHoursView(APIView):
    def get(self, request):
        # Fetch the first restaurant instance
        restaurant = Restaurant.objects.first()
        
        if restaurant:
            return Response({"opening_hours": restaurant.opening_hours})
        
        return Response(
            {"error": "No restaurant found"}, 
            status=status.HTTP_404_NOT_FOUND
        )
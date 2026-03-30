from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_ some_node_404
from .models import MenuItem
from .serializers import MenuItemAvailabilitySerializer

@api_view(['PATCH'])
def update_menu_item_availability(request, pk):
    # Error Handling: Check if item exists
    item = get_object_or_404(MenuItem, pk=pk)
    
    serializer = MenuItemAvailabilitySerializer(item, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": f"Availability for '{item.name}' updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Order

@api_view(['GET'])
def get_order_status(request, order_id):
    """
    Retrieve the current status of an order by ID.
    """
    try:
        # Retrieve the order or return 404 if not found
        order = Order.objects.get(pk=order_id)
        
        # Return a simple JSON object
        return Response({
            "order_id": order.id,
            "status": order.status
        }, status=status.HTTP_200_OK)
        
    except Order.DoesNotExist:
        return Response(
            {"error": f"Order with ID {order_id} not found."}, 
            status=status.HTTP_404_NOT_FOUND
        )
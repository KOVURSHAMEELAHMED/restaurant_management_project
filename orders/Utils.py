import logging
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Order

# Set up logger
logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status):
    """
    Utility function to update the status of a specific order.
    """
    try:
        # Retrieve the order
        order = Order.objects.get(pk=order_id)
        
        old_status = order.status
        order.status = new_status
        order.save()

        # Log the successful update
        logger.info(f"Order {order_id} updated: {old_status} -> {new_status}")
        return True, order

    except Order.DoesNotExist:
        logger.error(f"Failed to update status: Order {order_id} not found.")
        return False, "Order not found"
    
    except Exception as e:
        logger.error(f"Unexpected error updating order {order_id}: {str(e)}")
        return False, str(e)
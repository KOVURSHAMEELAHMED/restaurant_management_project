from django.urls import path
from .views import get_order_status

urlpatterns = [
    # Path parameter <int:order_id> matches the argument in the view
    path('orders/<int:order_id>/status/', get_order_status, name='order-status'),
]
from django.urls import path
from .views import UpdateOrderItemQuantityView

urlpatterns = [
    # Example: /api/order-items/123/update-quantity/
    path('order-items/<int:pk>/update-quantity/', UpdateOrderItemQuantityView.as_view(), name='update-order-item'),
]
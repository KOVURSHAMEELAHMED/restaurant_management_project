from django.urls import path
from .views import OrderStatusUpdateView

urlpatterns = [
    path('orders/<int:pk>/status/', OrderStatusUpdateView.as_view(), name='update-order-status'),
]
from django.urls import path
from .views import OrderStatusUpdateView

urlpatterns = [
    path('order/<int:pk>/update-status/', OrderStatusUpdateView.as_view(), name='update-order-status'),
]
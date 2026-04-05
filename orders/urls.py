from django.urls import path
from .views import UserOrderHistoryView

urlpatterns = [
    path('history/', UserOrderHistoryView.as_view(), name='user-order-history'),
]
from django.urls import path
from .views import PaymentMethodListView

urlpatterns = [
    # ... existing urls ...
    path('api/payment-methods/', PaymentMethodListView.as_view(), name='payment-method-list'),
]
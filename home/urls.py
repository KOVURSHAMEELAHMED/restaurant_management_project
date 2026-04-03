from django.urls import path
from .views import RestaurantHoursView

urlpatterns = [
    # ... existing paths ...
    path('api/hours/', RestaurantHoursView.as_view(), name='restaurant-hours'),
]
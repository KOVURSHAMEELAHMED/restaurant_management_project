from django.urls import path
from .views import FeaturedMenuItemsAPIView

urlpatterns = [
    path('api/menu/featured/', FeaturedMenuItemsAPIView.as_view(), name='featured-menu-items'),
]
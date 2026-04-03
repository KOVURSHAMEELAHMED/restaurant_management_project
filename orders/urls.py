from django.urls import path
from .views import MenuItemListView, MenuItemDetailView

urlpatterns = [
    path('api/menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    # New detail endpoint
    path('api/menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
]
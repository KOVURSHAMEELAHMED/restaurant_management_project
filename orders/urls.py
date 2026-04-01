from django.urls import path
from .views import MenuItemSearchView

urlpatterns = [
    # Usage: /api/menu/search/?q=pizza
    path('api/menu/search/', MenuItemSearchView.as_view(), name='menu-item-search'),
]
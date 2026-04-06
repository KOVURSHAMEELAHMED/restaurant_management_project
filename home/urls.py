from django.urls import path
from .views import MenuItemCountView

urlpatterns = [
    path('api/menu/count/', MenuItemCountView.as_view(), name='menu-item-count'),
]
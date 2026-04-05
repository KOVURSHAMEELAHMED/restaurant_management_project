from django.urls import path
from .views import AvailableMenuItemsView

urlpatterns = [
    path('menu/available/', AvailableMenuItemsView.as_view(), name='available-menu-items'),
]
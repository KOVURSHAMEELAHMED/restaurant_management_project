from django.urls import path
from .views import AvailableTablesAPIView

urlpatterns = [
    # Map the URL to our new view
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
]
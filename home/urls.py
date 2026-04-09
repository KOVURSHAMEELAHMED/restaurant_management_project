from django.urls import path
from . import views

urlpatterns = [
    path('api/tables/', views.TableListView.as_view(), name='table-list'),
    # Optional: Only available tables endpoint
    path('api/tables/available/', views.AvailableTablesView.as_view(), name='available-tables'),
]
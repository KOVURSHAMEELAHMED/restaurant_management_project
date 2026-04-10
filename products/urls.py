from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# For ListAPIView
urlpatterns = [
    path('api/cuisines/', views.CuisineListView.as_view(), name='cuisine-list'),
]

# If using ViewSet, you would do:
# router = DefaultRouter()
# router.register(r'api/cuisines', views.CuisineViewSet, basename='cuisine')
# urlpatterns = [
#     path('', include(router.urls)),
# ]
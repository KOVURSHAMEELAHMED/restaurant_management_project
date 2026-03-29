from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet

# Routers automatically map the standard CRUD actions to URL patterns
router = DefaultRouter()
router.register(r'categories', MenuCategoryViewSet, basename='menucategory')

urlpatterns = [
    path('', include(router.urls)),
]
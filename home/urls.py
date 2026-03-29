from django.urls import path
from .views import UserReviewListCreateView

urlpatterns = [
    path('reviews/', UserReviewListCreateView.as_view(), name='review-list-create'),
]
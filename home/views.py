from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Review
from .serializers import ReviewSerializer

class ReviewPagination(PageNumberPagination):
    page_size = 10  # Number of reviews per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination

from rest_framework import generics
from .models import OpeningHour
from .serializers import OpeningHourSerializer

class OpeningHourListView(generics.ListAPIView):
    queryset = OpeningHour.objects.all()
    serializer_class = OpeningHourSerializer
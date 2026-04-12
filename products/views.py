
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListView(generics.ListAPIView):
    # Fetch all feedback, ordered by 'created_at' descending
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
from rest_framework import generics, permissions
from .models import UserReview
from .serializers import UserReviewSerializer

class MenuItemReviewCreateView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the review
        serializer.save(user=self.request.user)
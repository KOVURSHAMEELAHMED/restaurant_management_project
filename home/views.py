from rest_framework import generics
from .models import UserReview
from .serializers import UserReviewSerializer

class UserReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = UserReviewSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned reviews to a given menu item,
        by filtering against a `menu_item` query parameter in the URL.
        """
        queryset = UserReview.objects.all()
        menu_item_id = self.request.query_params.get('menu_item')
        if menu_item_id is not None:
            queryset = queryset.filter(menu_item_id=menu_item_id)
        return queryset

    def perform_create(self, serializer):
        # Automatically set the user to the currently logged-in user
        serializer.save(user=self.request.user)
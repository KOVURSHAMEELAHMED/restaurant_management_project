from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserLoyaltySerializer

class UserLoyaltyView(generics.RetrieveAPIView):
    serializer_class = UserLoyaltySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Returns the user profile/model of the person logged in
        return self.request.user
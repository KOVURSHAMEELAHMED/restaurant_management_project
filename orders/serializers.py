from rest_framework import serializers
from .models import UserReview

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id', 'rating', 'comment', 'menu_item']
        read_only_fields = ['user'] # User is taken from the request context
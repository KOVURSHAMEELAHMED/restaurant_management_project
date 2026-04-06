from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # This pulls the 'username' from the related User model
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'user_name', 'rating', 'comment', 'created_at']
from rest_framework import serializers
from .models import ContactFormSubmission

class ContactFormSubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactFormSubmission
        fields = ['id', 'name', 'email', 'message']

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters.")
        return value
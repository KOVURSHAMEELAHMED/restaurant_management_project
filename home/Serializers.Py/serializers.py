from rest_framework import serializers
from .models import OpeningHour

class OpeningHourSerializer(serializers.ModelSerializer):
    day_name = serializers.CharField(source='get_day_display', read_only=True)

    class Meta:
        model = OpeningHour
        fields = ['day_name', 'opening_time', 'closing_time', 'is_closed']
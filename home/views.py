from rest_framework import generics
from .models import Table
from .serializers import TableSerializer

class AvailableTablesAPIView(generics.ListAPIView):
    # Filter the queryset so only available tables are returned
    queryset = Table.objects.filter(is_available=True)
    serializer_class = TableSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Table
from .serializers import TableSerializer

# Option 1: Using ListAPIView (simpler, recommended)
class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# Option 2: Using APIView (more control)
class TableListAPIView(APIView):
    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

# Option 3: Only show available tables
class AvailableTablesView(generics.ListAPIView):
    serializer_class = TableSerializer
    
    def get_queryset(self):
        return Table.objects.filter(is_available=True)
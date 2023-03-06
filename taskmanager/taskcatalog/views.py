from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ("due_date", "priority", "status")
    search_fields = ("title")
    ordering_fields = ("due_date", "priority", "status")

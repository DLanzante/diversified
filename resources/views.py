from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Resource
from .serializers import ResourceSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['published_date']  # Allow filtering by published date
    search_fields = ['title', 'description']  # Allow searching by title and description
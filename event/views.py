from django.shortcuts import render
from event.models import Event
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from event.serializers import EventSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

@method_decorator(cache_page(60 * 15), name='dispatch')
class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fields = ['id', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

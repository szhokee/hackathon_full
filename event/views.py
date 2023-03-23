from django.shortcuts import render
from feedback.models import Like, Rating
from feedback.serializers import RatingSerializer
from event.models import Event
from event.serializers import EventSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

@method_decorator(cache_page(60 * 15), name='dispatch')
class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.get_queryset().order_by('id')
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['id']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs): 
        user = request.user
        like_obj, _ = Like.objects.get_or_create(owner=user, event_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'

        if not like_obj.is_like:  
            status = 'unliked'

        return Response({'status': status})
    
    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, event_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)

from django.shortcuts import render

from news.models import News
from rest_framework import viewsets 
from news.serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class NewsModelsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permision_classes = [IsAuthenticatedOrReadOnly]

# Create your views here.

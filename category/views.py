from django.shortcuts import render
from category.models import Category, Soup
from rest_framework import viewsets
from category.serializers import CategorySerializer, SoupSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Soup.objects.all()
    serializer_class = SoupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

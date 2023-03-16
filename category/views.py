from django.shortcuts import render
from category.models import Category
from rest_framework import viewsets
from category.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




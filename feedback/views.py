from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from feedback.models import Favorite
from feedback.serializers import FavoriteSeriaLizer
from rest_framework.permissions import IsAuthenticated



class FavoriteModelViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):

    gueryset = Favorite.objects.all()
    serializer_class = FavoriteSeriaLizer
    permission_classes =[IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        quereset = super().get_queryset()
        quereset = quereset.filter(owner=self.user)
        return quereset

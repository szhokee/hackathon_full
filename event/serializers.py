from django.db.models import Avg
from rest_framework import serializers
from event.models import Event
from feedback.serializers import LikeSerializer


class EventSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['like_count'] = instance.likes.filter(is_like=True).count()
        representation['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return representation

from rest_framework import serializers
from .models import Like, Rating, Favorite, Comment

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        Fields = '__all__'

class FavoriteSeriaLizer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
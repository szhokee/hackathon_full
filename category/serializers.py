from rest_framework import serializers
from category.models import Category, Soup


class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = '__all__'


class SoupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Soup
        fields = '__all__'



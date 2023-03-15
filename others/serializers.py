from rest_framework import serializers
from others.models import News, Bul, Cash_Register


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        filds = '__all__'

class BulSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bul
        filds = '__all__'
    
class Cash_RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cash_Register
        filds = '__all__'


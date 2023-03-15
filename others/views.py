from rest_framework import generics
from others.models import News, Bul, Cash_Register
from rest_framework import ViewSet, ModelViewSet
from rest_framework import NewsSerialiser 
from feedback.models import IsOwner
# Create your views here.
class NewsModelVieSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerialiser
    permision_classes = [IsOwner]

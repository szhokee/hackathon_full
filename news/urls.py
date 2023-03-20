from django.urls import path,  include
from news.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('news', NewsModelsViewSet)


urlpatterns = [
    path('news/', ),
   
]
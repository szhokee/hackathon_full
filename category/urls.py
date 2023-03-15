from django.urls import path, include
from rest_framework.routers import DefaultRouter
from category.views import *

router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('events', EventModelViewSet)


urlpatterns = [
    # path('category/', CategoryAPIView.as_view()),
]
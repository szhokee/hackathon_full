from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import *

router = DefaultRouter()

router.register('event', EventModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]

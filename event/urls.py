from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import *

router = DefaultRouter()

router.register('', EventModelViewSet)

urlpatterns = [
    path('event/', include(router.urls))
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import *

router = DefaultRouter()

router.register('events', EventModelViewSet)

urlpatterns = [
    # path('event/', EventModelViewSet.as_view({'get':'list', 'post':'create'})),
    path('', include(router.urls))
]
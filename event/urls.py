from rest_framework.routers import DefaultRouter
from event.views import *

router = DefaultRouter()

router.register('events', EventModelViewSet)

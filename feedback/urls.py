from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback.views import FavoriteModelViewSet

router = DefaultRouter()
router.register('', FavoriteModelViewSet)

urlpatterns = [
    path('')
]

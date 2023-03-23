from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback.views import *

router = DefaultRouter()
router.register('rating', RatingModelViewSet)
router.register('comment', CommentModelViewSet)
router.register('favorite', FavoriteModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]

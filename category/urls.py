from django.urls import path, include
from rest_framework.routers import DefaultRouter
from category.views import *

router = DefaultRouter()
router.register('category', CategoryAPIView)

urlpatterns = [
    path('', include(router.urls)),
]

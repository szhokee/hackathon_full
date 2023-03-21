from django.urls import path, include
from rest_framework.routers import DefaultRouter
from category.views import *

router = DefaultRouter()
router.register('', CategoryAPIView)

urlpatterns = [
    path('category/', include(router.urls)),
]

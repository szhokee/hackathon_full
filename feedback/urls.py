from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback.views import FavoriteModelViewSet

router = DefaultRouter()
router.register('', FavoriteModelViewSet)

urlpatterns = [
    path('favorite/', include(router.urls)),
    path('rating/', include(router.urls)),
    path('like/', include(router.urls))
]
# urlpatterns += router.urls

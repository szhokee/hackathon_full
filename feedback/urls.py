from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback.views import FavoriteModelViewSet

router = DefaultRouter()
router.register('favorite', FavoriteModelViewSet)

urlpatterns = [
    path('rating/', include(router.urls)),
    path('like/', include(router.urls)),
    path('comment/', include(router.urls)),
    path('', include(router.urls))
]
# urlpatterns += router.urls

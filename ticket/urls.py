from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ticket.views import *

router = DefaultRouter()
router.register('apiview_get_post', TicketViewSet, basename='products')
router.register('modelviewset_crud', TicketModelViewSet)
router.register('product_mixin', TicketMixin)
router.register('category', CategoryAPIView)

urlpatterns = [
    path('func_get/', get_product),
    path('func_post/', post_product),

    path('generic_get/', TicketListGenericView.as_view()),
    path('generic_post/', TicketCreateGenericView.as_view()),
    path('generic_get_post/', TicketListCreateGenericView.as_view()),

    path('apiview_get_post/', TicketAPIView.as_view()),

    path('viewset_get_post/', TicketViewSet.as_view({'get':'list', 'post':'create'})),

    path('hello/', get_hello),

    path('', include(router.urls))

]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from ticket.views import TicketOrderModelViewset, TicketConfirmAPIView

router = DefaultRouter()
router.register('', TicketOrderModelViewset)

urlpatterns = [
    path('confirm/<uuid:code>/', TicketConfirmAPIView.as_view()),
    path('', include(router.urls))
]

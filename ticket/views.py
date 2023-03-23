from rest_framework.viewsets import ModelViewSet
from ticket.models import Ticket
from ticket.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class TicketOrderModelViewset(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user.id)
        return queryset

class TicketConfirmAPIView(APIView):
    def get(self, request, code):
        ticket = get_object_or_404(Ticket, activation_code=code)
        if not ticket.confirm:
            ticket.confirm = True
            ticket.save(update_fields=['confirm', 'activation_code'])
            return Response({'message': 'Successful confirmation of your order!'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already confirmed your order'}, status=status.HTTP_400_BAD_REQUEST)

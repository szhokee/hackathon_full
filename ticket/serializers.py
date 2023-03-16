from rest_framework import serializers
from ticket.models import Ticket



class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'

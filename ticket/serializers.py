from rest_framework import serializers
from ticket.models import Ticket
from ticket.tasks import send_ticket_confirmation_code

class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        amount = validated_data.get('amount')
        event = validated_data.get('event')

        if amount > event.amount:
            raise serializers.ValidationError('Not enough tickets in event')
        if amount == 0:
            raise serializers.ValidationError('Tickets can not be 0')

        event.amount -= amount
        event.save(update_fields=['amount'])

        ticket = Ticket.objects.create(**validated_data)

        send_ticket_confirmation_code(ticket.owner.email, ticket.activation_code, ticket.event.title, ticket.total_price)

        return ticket

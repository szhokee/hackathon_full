from rest_framework import serializers
from ticket.models import Ticket, Category



class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    class Meta:
        model = Category
        fields = '__all__'
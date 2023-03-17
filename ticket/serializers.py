from rest_framework import serializers
from ticket.models import Ticket
<<<<<<< HEAD


=======
>>>>>>> fc6d09d457f87d025421b60ac145a0f38a6188fd

class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    
    class Meta:
        model = Ticket
        fields = '__all__'
<<<<<<< HEAD

=======
>>>>>>> fc6d09d457f87d025421b60ac145a0f38a6188fd

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins
from rest_framework.views import APIView


from category.models import Category
from ticket.models import Ticket

from ticket.serializers import TicketSerializer
from ticket.tasks import big_function
from category.serializers import CategorySerializer

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




@api_view(['GET'])
def get_product(request):
    """
    Get all product
    """
    products = Ticket.objects.all()
    serializer = TicketSerializer(products, many=True)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_product(request):
    # print(request.data)
    serializer = TicketSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(owner=request.user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# CLASSSSSSS

class TicketListGenericView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    

class TicketCreateGenericView(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



#GENERIIIC

class TicketListCreateGenericView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class TicketAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Ticket.objects.all()
        serializer = TicketSerializer(products, many=True)
        return Response(serializer.data)
        # return Response('geet')

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response('pooost')



#Viewset

class TicketViewSet(viewsets.ViewSet):
    def list(self, request):                 #get
        product = Ticket.objects.all()
        serializer = TicketSerializer(product, many=True)
        return Response(serializer.data)


    def create(self, request):                #post
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)



#MODELVIEWSET

class TicketModelViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



#Mixin

class TicketMixin(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                #    mixins.UpdateModelMixin,
                #    mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

@api_view(['GET'])
def get_hello(request):
    big_function.delay()
    # import time 
    # time.sleep(10)
    return Response('HELLO!!!')


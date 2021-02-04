from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from rest_framework.permissions import IsAdminUser
from .permission import IsOwnerOrReadOnly

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
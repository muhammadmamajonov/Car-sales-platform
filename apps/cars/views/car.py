from ..models.car import Car
from ..serializers.cars import *
from utils.permissions import IsOwner
from ..pagination import CarsListPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView



class CarPostAPIView(CreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class CarEditAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwner]
    http_method_names = ['patch']


class CarGetAPIView(RetrieveAPIView):
    authentication_classes = []
    queryset = Car.objects.all()
    serializer_class = CarGetDetailSerializer
    

class CarListAPIView(ListAPIView):
    authentication_classes = []
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    pagination_class = CarsListPagination


class CarsOwnedByOrientMotorsAPIView(ListAPIView):
    authentication_classes = []
    pagination_class = CarsListPagination
    serializer_class = CarsOwnedByOrientMotorsSerializer

    def get_queryset(self):
        self.queryset = Car.objects.filter(owned_by_orient_motors=True)
        return super().get_queryset()


class DiagnosedCarsListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = CarsListFilterByServiceSerializer
    queryset = Car.objects.filter(avtoritet_diagnostics=True).select_related("model", "model__brand")


class PremiumDiagnosedCarsListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = CarsListFilterByServiceSerializer
    queryset = Car.objects.filter(avtoritet_premium_diagnostics=True).select_related("model", "model__brand")


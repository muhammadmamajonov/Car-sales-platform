from ..models import Car
from ..serializers.cars import *
from utils.permissions import IsOwner
from ..pagination import CarsListPagination
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

authentication_classes = [SessionAuthentication, JWTAuthentication]


class CarPostAPIView(CreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = authentication_classes


class CarEditAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwner]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class CarGetAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarGetDetailSerializer
    

class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    pagination_class = CarsListPagination


class CarsOwnedByOrientMotorsAPIView(ListAPIView):
    pagination_class = CarsListPagination
    serializer_class = CarsOwnedByOrientMotorsSerializer

    def get_queryset(self):
        self.queryset = Car.objects.filter(owned_by_orient_motors=True)
        return super().get_queryset()


# class CarsFilterAPIView(ListAPIView):
#     serializer_class = CarListSerializer
    

#     def list(self, request, *args, **kwargs):
#         brand = request.data.get('brand')    
#         model = request.data.get('model')

#         if not model:
#             self.queryset = Car.objects.

#         return super().list(request, *args, **kwargs)
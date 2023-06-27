from ..models import Fuel
from ..serializers.fuel import *
from rest_framework.permissions import IsAdminUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView


authentication_classes = [SessionAuthentication, JWTAuthentication]

class FuelCreateAPIView(CreateAPIView):
    serializer_class = FuelSerializer
    permission_classes = [IsAdminUser]
    authentication_classes=authentication_classes


class FuelEditAPIView(UpdateAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class FuelGetAPIView(RetrieveAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    

class FuelListAPIView(ListAPIView):
    serializer_class = FuelListSerializer

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Fuel.objects.language(language).all()
        return super().get_queryset()
from ..models import Fuel
from ..serializers.fuel import *
from utils.permissions import IsSuperUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView

authentication_classes = [SessionAuthentication, JWTAuthentication]

class FuelAddAPIView(CreateAPIView):
    serializer_class = FuelSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes=authentication_classes


class FuelRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes
    http_method_names = ('patch', 'get')
    

class FuelListAPIView(ListAPIView):
    serializer_class = FuelListSerializer
    queryset = Fuel.objects.all()
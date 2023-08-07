from ..models import Fuel
from ..serializers.fuel import *
from utils.permissions import IsSuperUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class FuelAddAPIView(CreateAPIView):
    serializer_class = FuelSerializer
    permission_classes = (IsSuperUser,)


class FuelRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    permission_classes = (IsSuperUser,)
    http_method_names = ('patch', 'get')
    

class FuelListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = FuelListSerializer
    queryset = Fuel.objects.all()
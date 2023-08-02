from ..models import Transmission
from utils.permissions import IsSuperUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from ..serializers.transmission import TransmissionListSerializer, TransmissionSerializer


authentication_classes = (SessionAuthentication, JWTAuthentication)


class TransmissionAddAPIView(CreateAPIView):
    serializer_class = TransmissionSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes


class TransmissionRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TransmissionSerializer
    queryset = Transmission.objects.all()
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes
    http_method_names = ('get', 'patch')


class TransmissionsListAPIView(ListAPIView):
    serializer_class = TransmissionListSerializer
    queryset = Transmission.objects.all()

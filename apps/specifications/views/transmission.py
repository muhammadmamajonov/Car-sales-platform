from ..models import Transmission
from utils.permissions import IsSuperUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from ..serializers.transmission import TransmissionListSerializer, TransmissionSerializer



class TransmissionAddAPIView(CreateAPIView):
    serializer_class = TransmissionSerializer
    permission_classes = (IsSuperUser,)


class TransmissionRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TransmissionSerializer
    queryset = Transmission.objects.all()
    permission_classes = (IsSuperUser,)
    http_method_names = ('get', 'patch')


class TransmissionsListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = TransmissionListSerializer
    queryset = Transmission.objects.all()

from ..models import Transmission
from ..serializers.transmission import *
from rest_framework.permissions import IsAdminUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView


authentication_classes = [SessionAuthentication, JWTAuthentication]


class TransmissionCreateAPIView(CreateAPIView):
    serializer_class = TransmissionSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes


class TransmissionEditAPIView(UpdateAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class TransmissionGetAPIView(RetrieveAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer


class TransmissionListAPIView(ListAPIView):
    serializer_class = TransmissionListSerializer

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Transmission.objects.language(language).all()
        return super().get_queryset()
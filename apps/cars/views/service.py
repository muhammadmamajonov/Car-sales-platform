from ..models import Service
from rest_framework.permissions import IsAdminUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.service import ServiceListSerializer, ServiceSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView


authentication_classes = [SessionAuthentication, JWTAuthentication]


class ServiceCreateAPIView(CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes


class ServiceEditAPIView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class ServiceGetAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Service.objects.language(language).all()
        return super().get_queryset()

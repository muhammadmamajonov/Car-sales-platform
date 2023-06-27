from ..models import Color
from rest_framework.permissions import IsAdminUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from ..serializers.color import ColorSerializer, ColorListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView


authentication_classes = [SessionAuthentication, JWTAuthentication]


class ColorCreateAPIView(CreateAPIView):
    serializer_class = ColorSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class ColorEditAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class ColorGetAPIView(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorListAPIView(ListAPIView):
    serializer_class = ColorListSerializer

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Color.objects.language(language).all()
        return super().get_queryset()

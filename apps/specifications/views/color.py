from ..models import Color
from utils.permissions import IsSuperUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.color import ColorListSerializer, ColorSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


authentication_classes = (SessionAuthentication, JWTAuthentication)

class ColorAddAPIView(CreateAPIView):
    serializer_class = ColorSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes


class ColorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes


class ColorListAPIView(ListAPIView):
    serializer_class = ColorListSerializer
    queryset = Color.objects.all()



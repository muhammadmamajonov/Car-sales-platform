from ..models import Color
from utils.permissions import IsSuperUser
from ..serializers.color import ColorListSerializer, ColorSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView



class ColorAddAPIView(CreateAPIView):
    serializer_class = ColorSerializer
    permission_classes = (IsSuperUser,)


class ColorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = (IsSuperUser,)


class ColorListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = ColorListSerializer
    queryset = Color.objects.all()



from ..models import BodyType
from utils.permissions import IsSuperUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.body_type import BodyTypeListSerializer, BodyTypeSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


authentication_classes = (SessionAuthentication, JWTAuthentication)

class BodyTypeAddAPIView(CreateAPIView):
    serializer_class = BodyTypeSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes


class BodyTypeRetieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BodyTypeSerializer
    queryset = BodyType.objects.all()
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes


class BodyTypeListAPIView(ListAPIView):
    serializer_class = BodyTypeListSerializer
    queryset = BodyType.objects.all()



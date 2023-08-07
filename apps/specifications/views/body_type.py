from ..models import BodyType
from utils.permissions import IsSuperUser
from ..serializers.body_type import BodyTypeListSerializer, BodyTypeSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView



class BodyTypeAddAPIView(CreateAPIView):
    serializer_class = BodyTypeSerializer
    permission_classes = (IsSuperUser,)


class BodyTypeRetieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BodyTypeSerializer
    queryset = BodyType.objects.all()
    permission_classes = (IsSuperUser,)


class BodyTypeListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = BodyTypeListSerializer
    queryset = BodyType.objects.all()



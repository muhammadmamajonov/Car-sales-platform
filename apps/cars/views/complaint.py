from rest_framework.generics import CreateAPIView, ListAPIView
from ..models.complaint import Complaints, Reason
from rest_framework.permissions import IsAuthenticated
from ..serializers.complaint import ReasonsListSerializer, ComplaintsSerialzier

class ReasonsListAPIView(ListAPIView):
    serializer_class = ReasonsListSerializer
    queryset = Reason.objects.all()
    authentication_classes = []


class ComplaintPostAPIView(CreateAPIView):
    serializer_class = ComplaintsSerialzier
    permission_classes = (IsAuthenticated,)

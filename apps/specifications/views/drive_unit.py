from ..models import DriveUnit
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.drive_unit import DriveUnitListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from django.utils.translation import get_language_from_request


class DriveUnitListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = DriveUnitListSerializer

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = DriveUnit.objects.language(language).all()
        return super().get_queryset()

from ..models import VehicleOptions
from utils.permissions import IsSuperUser
from django.utils.translation import get_language_from_request
from ..serializers.vehicle_options import VehicleOptionsListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class VehicleOptionsListAPIView(ListAPIView):
    serializer_class = VehicleOptionsListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = VehicleOptions.objects.language(language).all()
        return super().get_queryset()
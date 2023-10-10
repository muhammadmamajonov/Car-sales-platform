from ..models import Salon
from utils.permissions import IsSuperUser
from ..serializers.salon import SalonListSerializer
from django.utils.translation import get_language_from_request
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class SalonListAPIView(ListAPIView):
    serializer_class = SalonListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Salon.objects.language(language).all()
        return super().get_queryset()
    
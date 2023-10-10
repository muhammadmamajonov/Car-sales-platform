from ..models import Optics
from utils.permissions import IsSuperUser
from ..serializers.optics import OpticsListSerializer
from django.utils.translation import get_language_from_request
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class OpticsListAPIView(ListAPIView):
    serializer_class = OpticsListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Optics.objects.language(language).all()
        return super().get_queryset()
from ..models import ExternalBodyKit
from utils.permissions import IsSuperUser
from ..serializers.external_body_kit import ExternalBodyKitListSerializer
from django.utils.translation import get_language_from_request
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class ExternalBodyKitListAPIView(ListAPIView):
    serializer_class = ExternalBodyKitListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = ExternalBodyKit.objects.language(language).all()
        return super().get_queryset()
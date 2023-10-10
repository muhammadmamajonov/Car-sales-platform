from ..models import MediaTools
from utils.permissions import IsSuperUser
from ..serializers.media_tools import MediaToolsListSerializer
from django.utils.translation import get_language_from_request
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class MediaToolsListAPIView(ListAPIView):
    serializer_class = MediaToolsListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = MediaTools.objects.language(language).all()
        return super().get_queryset()
    
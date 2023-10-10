from ..models import MediaTools
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class MediaToolsListSerializer(TranslatableModelSerializer):
    class Meta:
        model = MediaTools
        fields = ('id', 'title')
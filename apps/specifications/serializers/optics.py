from ..models import Optics
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class OpticsListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Optics
        fields = ('id', 'title')
        
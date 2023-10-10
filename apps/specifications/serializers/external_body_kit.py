from ..models import ExternalBodyKit
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class ExternalBodyKitListSerializer(TranslatableModelSerializer):
    class Meta:
        model = ExternalBodyKit
        fields = ('id', 'title')
        
        

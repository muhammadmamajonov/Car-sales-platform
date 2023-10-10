from ..models import Salon
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class SalonListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'title')
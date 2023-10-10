from ..models import VehicleOptions
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class VehicleOptionsListSerializer(TranslatableModelSerializer):
    class Meta:
        model = VehicleOptions
        fields = ('id', 'title')
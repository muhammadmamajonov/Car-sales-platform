from ..models import Region
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer

class RegionSerializer(TranslatableModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
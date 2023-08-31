from ..models import Color
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

class ColorSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Color, help_text="{'ru': {'name': 'Белый'},'uz': {'name': 'Oq'}}")

    class Meta:
        model = Color
        fields = ['translations', 'code']


class ColorListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'code']

    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)

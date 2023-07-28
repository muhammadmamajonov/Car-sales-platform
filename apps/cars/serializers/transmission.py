from ..models.specification import Transmission, Color
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class TransmissionSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Color, help_text="{'ru': {'name': 'Автамат'},'uz': {'name': 'Avtamat'}}")
    class Meta:
        model = Transmission
        fields = '__all__'
    

class TransmissionListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Transmission
        fields = ['id', 'name']

    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
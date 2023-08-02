from ..models import BodyType
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

class BodyTypeSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=BodyType, help_text="{'ru': {'name': 'Седан'},'uz': {'name': 'Sedan'}}")
    class Meta:
        model = BodyType
        fields = ['translations']


class BodyTypeListSerializer(TranslatableModelSerializer):
    class Meta:
        model = BodyType
        fields = ['id', 'name']
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
    

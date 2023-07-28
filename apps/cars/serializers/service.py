from ..models.service import *
from ..models.specification import Color
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class ServiceSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Color, help_text="{'ru': {'name': 'service ru'},'uz': {'name': 'service uz'}}")
    
    class Meta:
        model = Service
        fields = '__all__'


class ServiceListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
from ..models.specification import *
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

class FuelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Fuel,  help_text="{'ru': {'name': 'Бензин'},'uz': {'name': 'Benzin'}}")
    class Meta:
        model = Fuel
        fields = '__all__'


class FuelListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Fuel
        fields = ['id', 'name']

    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
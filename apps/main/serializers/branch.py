
from apps.main.models import Branch
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class BranchSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Branch)

    class Meta:
        model = Branch
        fields = '__all__'

    
class BranchListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'address', 'contact', 'working_time', 'address', 'lat', 'long')

    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
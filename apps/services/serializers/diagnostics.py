from ..models.diagnostics import DiagnosticsFAQ, DiagnosticsInfo
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class DiagnosticsInfoSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=DiagnosticsInfo, help_text="{'ru': {'title': 'title ru', 'description':'description ru'},'uz': {'title': 'title uz', 'description':'description uz'}}")
    
    class Meta:
        model = DiagnosticsInfo
        fields = '__all__'


class DiagnosticsInfoListSerializer(TranslatableModelSerializer):
    class Meta:
        model = DiagnosticsInfo
        fields = ('title', 'description', 'photo')
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
    
# FAQ

class DiagnosticsFAQSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=DiagnosticsFAQ, help_text="{'ru': {'question': 'question ru', 'answer':'answer ru'},'uz': {'question': 'question uz', 'answer':'answer uz'}}")

    class Meta:
        model = DiagnosticsFAQ
        fields = '__all__'


class DiagnosticsFAQListSerializer(TranslatableModelSerializer):
    class Meta:
        model = DiagnosticsFAQ
        fields = ('question', 'answer')
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
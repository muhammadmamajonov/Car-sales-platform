from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from ..models.premium_diagnostics import DiagnosticSpecialists, PremiumDiagnosticsFAQ, PremiumDiagnosticsInfo, SpecialDiagnosticEquipment


class PremiumDiagnosticsInfoSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=PremiumDiagnosticsInfo, help_text="{'ru': {'title': 'title ru', 'description':'description ru'},'uz': {'title': 'title uz', 'description':'description uz'}}")
    
    class Meta:
        model = PremiumDiagnosticsInfo
        fields = '__all__'


class PremiumDiagnosticsInfoListSerializer(TranslatableModelSerializer):
    class Meta:
        model = PremiumDiagnosticsInfo
        fields = ('title', 'description', 'photo')
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
    
# FAQ

class PremiumDiagnosticsFAQSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=PremiumDiagnosticsFAQ, help_text="{'ru': {'question': 'question ru', 'answer':'answer ru'},'uz': {'question': 'question uz', 'answer':'answer uz'}}")

    class Meta:
        model = PremiumDiagnosticsFAQ
        fields = '__all__'


class PremiumDiagnosticsFAQListSerializer(TranslatableModelSerializer):
    class Meta:
        model = PremiumDiagnosticsFAQ
        fields = ('question', 'answer')
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)


# Special diagnostics Equipent

class SpecialDiagnosticEquipmentSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SpecialDiagnosticEquipment, help_text="{'ru': {'title': 'title ru', 'description':'description ru'},'uz': {'title': 'title uz', 'description':'description uz'}}")
    
    class Meta:
        model = SpecialDiagnosticEquipment
        fields = ('translations', 'photo')


class SpecialDiagnosticEquipmentListSerializer(TranslatableModelSerializer):
    class Meta:
        model = SpecialDiagnosticEquipment
        fields = ('title', 'descipription', 'photo')
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
    

# specialists

class DiagnosticSpecialistsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField()
    class Meta:
        model = DiagnosticSpecialists
        fields = ('id', 'translations', 'experience', 'photo')


class DiagnosticSpecialistsListSerializer(TranslatableModelSerializer):
    class Meta:
        model = DiagnosticSpecialists
        fields = ('full_name', 'specialty', 'experience', 'photo')

    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
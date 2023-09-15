from rest_framework.serializers import SerializerMethodField
from django.utils.translation import get_language_from_request
from parler_rest.serializers import TranslatableModelSerializer
from ..models.review import SafetyAndConvenience, SafetyAndConvenienceAdvantages


class SafetyAndConvenienceAdvantagesGetSerializer(TranslatableModelSerializer):
    class Meta:
        model = SafetyAndConvenienceAdvantages
        fields = ('text',)


class SafetyConvenienceGetSerializer(TranslatableModelSerializer):
    advantages = SerializerMethodField()

    class Meta:
        model = SafetyAndConvenience
        fields = ('safety_equipment', 'convenience_equipment', 'rated_by_orient_motors', 'photo', 'advantages')

    def get_advantages(self, obj):
        language = get_language_from_request(self.context['request'])
        advantages = obj.advantages.language(language).all()
        data = SafetyAndConvenienceAdvantagesGetSerializer(advantages, many=True).data
        return data
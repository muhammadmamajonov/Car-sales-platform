from rest_framework.serializers import SerializerMethodField
from parler_rest.serializers import TranslatableModelSerializer
from ..models.review_performance import Performance, PerformanceAdvantages, PerformanceFlaws



class PerformanceAdvantagesSerializer(TranslatableModelSerializer):
    class Meta:
        model = PerformanceAdvantages
        fields = ('title', 'rated')


class PerformanceFlawsSerializer(TranslatableModelSerializer):
    class Meta:
        model = PerformanceFlaws
        fields = ('title', 'rated')


class PerformanceSerializer(TranslatableModelSerializer):
    flaws = SerializerMethodField()
    advantages = SerializerMethodField()

    class Meta:
        model = Performance
        fields = ('title', 'direct_driving', 'curved_driving', 'rated_by_orient_motors', 'photo', 'advantages', 'flaws')

    
    def get_flaws(self, obj):
        flaws = obj.flaws.first()
        data = PerformanceFlawsSerializer(flaws).data
        return data

    def get_advantages(self, obj):
        advantages = obj.advantages.first()
        data = PerformanceAdvantagesSerializer(advantages).data
        return data
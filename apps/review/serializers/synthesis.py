from ..models.synthesis import Synthesis, CarReviewFAQ
from parler_rest.serializers import TranslatableModelSerializer



class SynthesisGetSerializer(TranslatableModelSerializer):
    class Meta:
        model = Synthesis
        fields = ('text', 'advantage', 'flaw')



class CarReviewFAQGetSerializer(TranslatableModelSerializer):
    class Meta:
        model = CarReviewFAQ
        fields = ('question', 'answer')
from ..models import PaintCondition
from parler_rest.serializers import TranslatableModelSerializer


class PaintConditionListSerializer(TranslatableModelSerializer):
    class Meta:
        model = PaintCondition
        fields = ('id', 'title')
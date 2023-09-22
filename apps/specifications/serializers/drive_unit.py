from ..models import DriveUnit
from parler_rest.serializers import TranslatableModelSerializer


class DriveUnitListSerializer(TranslatableModelSerializer):
    class Meta:
        model = DriveUnit
        fields = ('id', 'title')

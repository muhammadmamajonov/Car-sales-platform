from ..models.complaint import Complaints, Reason
from rest_framework.serializers import ModelSerializer
from parler_rest.serializers import TranslatableModelSerializer


class ReasonsListSerializer(TranslatableModelSerializer):
    class Meta:
        model = Reason
        fields = ('id', 'name')


class ComplaintsSerialzier(ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'
        


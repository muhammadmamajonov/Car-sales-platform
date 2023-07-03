from ..models import User
from rest_framework.serializers import ModelSerializer


class CarOwnerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'first_name']
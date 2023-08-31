from ..models import User
from rest_framework.serializers import ModelSerializer


class CarOwnerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'full_name']



class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'full_name', 'birthdate', 'sellertype', 'password')
        write_only_fields = ('password',)
from ..models.car import Car
from ..serializers.brand import  CarModelSerializer
from ...main.serializers.region import RegionSerializer
from ...users.serializers.user import CarOwnerSerializer
from apps.specifications.serializers.fuel import FuelListSerializer
from apps.specifications.serializers.color import ColorListSerializer
from apps.specifications.serializers.body_type import BodyTypeListSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ...specifications.serializers.transmission import TransmissionListSerializer


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['liked_by']


class CarGetDetailSerializer(ModelSerializer):
    region = RegionSerializer()
    fuel = FuelListSerializer()
    model = CarModelSerializer()
    owner = CarOwnerSerializer()
    color = ColorListSerializer()
    body_type = BodyTypeListSerializer()
    transmission = TransmissionListSerializer()

    class Meta:
        model = Car
        fields = '__all__'
        

    def to_representation(self, instance):
        re = super().to_representation(instance)
        re['likes'] = len(re['liked_by'])
        del re['liked_by']
        return re


class CarListSerializer(ModelSerializer):
    model = SerializerMethodField()
    liked = SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'model', 'year', 'price', 'currency', 'engine_size', 'mileage', 'liked']

    def get_model(self, obj):
        model = {
            'name':obj.model.name,
            'brand':obj.model.brand.name
        }
        return model
    
    def get_liked(self, obj):
        request = self.context.get('request')
        user = request.user
        if user in obj.liked_by.all():
            return True
        return False


class CarsOwnedByOrientMotorsSerializer(ModelSerializer):
    body_type = BodyTypeListSerializer()
    model = SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'model', 'body_type', 'rate']
    
    def get_model(self, obj):
        model = {
            'name':obj.model.name,
            'brand':obj.model.brand.name
        }
        return model
    

class CarsListFilterByServiceSerializer(ModelSerializer):
    liked = SerializerMethodField()
    model = SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'model', 'price', 'year', 'engine_size', 'horsepower', 'liked')

    def get_liked(self, obj):
        request = self.context.get('request')
        user = request.user
        if user in obj.liked_by.all():
            return True
        return False

    def get_model(self, obj):
        model = {
            'name':obj.model.name,
            'brand':obj.model.brand.name
        }
        return model    
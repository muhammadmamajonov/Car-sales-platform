from ..models.car import Car
from ...users.serializers.user import CarOwnerSerializer
from ...main.serializers.region import RegionListSerializer
from ..serializers.brand import  CarModelForCarDetailSerializer
from apps.specifications.serializers.fuel import FuelListSerializer
from apps.specifications.serializers.color import ColorListSerializer
from apps.specifications.serializers.body_type import BodyTypeListSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ...specifications.serializers.transmission import TransmissionListSerializer


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        extra_kwargs = {
            "mileage": {"help_text":"Пробег"},
            "body_type":{"help_text":"Тип кузова"},
            "drive_unit":{"help_textt":"Привод"},
        }
        read_only_fields = ['liked_by']



class CarListSerializer(ModelSerializer):
    model = SerializerMethodField()
    liked = SerializerMethodField()
    photo = SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'model', 'price', 'year', 'engine_size', 'mileage', 'liked', 'avtoritet_diagnostics', 'avtoritet_premium_diagnostics', 'orient_motors_warranty', "owned_by_orient_motors", 'photo')
        

    def get_photo(self, obj):
        car_photo = obj.photos.first()
        return  car_photo.photo.url if car_photo else ""
    
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


class CarDetailSerializer(ModelSerializer):
    fuel = FuelListSerializer()
    owner = CarOwnerSerializer()
    color = ColorListSerializer()
    liked = SerializerMethodField()
    region = RegionListSerializer()
    photos = SerializerMethodField()
    body_type = BodyTypeListSerializer()
    model = CarModelForCarDetailSerializer()
    transmission = TransmissionListSerializer()

    class Meta:
        model = Car
        fields = ('id', 'model', 'price', 'currency', 'year', 'month', 
                  'engine_size', 'mileage', 'liked', 'horsepower', 'used_car', 
                  'avtoritet_diagnostics', 'avtoritet_premium_diagnostics', 
                  'orient_motors_warranty', "owned_by_orient_motors", 'photos',
                  'rated', 'owner', 'body_type', 'region', 'fuel', 'transmission', 'color'
                )

    def get_photos(self, obj):
        return [photo.photo.url for photo in obj.photos.all()]
    
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
        fields = ['id', 'model', 'body_type', 'rated']
    
    def get_model(self, obj):
        model = {
            'name':obj.model.name,
            'brand':obj.model.brand.name
        }
        return model


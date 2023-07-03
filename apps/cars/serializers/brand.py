from ..models import Brand, Model, Car
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ['used']


class CarModelSerializer(ModelSerializer):
    brand = BrandSerializer()
    class Meta:
        model = Model
        fields = '__all__'
        read_only_fields = ['used']


class FilterBrandSerializer(ModelSerializer):
    count = SerializerMethodField()

    class Meta:
        model = Brand
        fields = ['id', 'name', 'icon', 'count']
    
    def get_count(self, obj):
        count = Car.objects.filter(model__brand_id=obj.id).count()
        return count
    

class FilterModelSerializer(ModelSerializer):
    count = SerializerMethodField()

    class Meta:
        model = Model
        fields = ['id', 'name', 'count']
    
    def get_count(self, obj):
        count = Car.objects.filter(model=obj).count()
        return count
from ..models.review import CarReview
from django.utils.translation import get_language_from_request
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CarReviewListSerializer(ModelSerializer):
    rated = SerializerMethodField()

    class Meta:
        model = CarReview
        fields = ('id', 'title', 'subtitle', 'photo', "rated")

    def get_rated(self, obj):
        rated_design = obj.design.first().rated_by_orient_motors
        rated_performance = obj.performance.first().rated_by_orient_motors
        rated_safety_convenience = obj.safety_convenience.first().rated_by_orient_motors
        rated_size_space = obj.size_space.first().rated_by_orient_motors
        rated_maintenance_management = obj.maintenance_management.first().rated_by_orient_motors
        sum = rated_design + rated_maintenance_management + rated_performance + rated_safety_convenience + rated_size_space
        rated = sum / 5
        return rated
    
    def to_representation(self, instance):
        language = get_language_from_request(self.context.get('request'))
        instance.set_current_language(language)
        return super().to_representation(instance)
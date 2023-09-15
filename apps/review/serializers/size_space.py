from ..models.size_and_space import SizeAndSpace
from rest_framework.serializers import SerializerMethodField
from parler_rest.serializers import TranslatableModelSerializer


class SizeSpaceGetSerializer(TranslatableModelSerializer):
    photos = SerializerMethodField()

    class Meta:
        model = SizeAndSpace
        fields = ('title', 'dimensions_and_space', 'rated_by_orient_motors', 'height_width_photo')
    
    def get_photos(self, obj):
        photos = [photo_obj.photo.url for photo_obj in obj.photos.all()]
        return photos
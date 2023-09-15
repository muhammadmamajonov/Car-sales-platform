from ..models.review_design import Design
from rest_framework.serializers import SerializerMethodField
from parler_rest.serializers import TranslatableModelSerializer



class ReviewDesignSerializer(TranslatableModelSerializer):
    external_photos = SerializerMethodField()
    interior_photos = SerializerMethodField()

    class Meta:
        model = Design
        fields = ('title', 'external_design', 'interior_design', 'rated_by_orient_motors', 'photo', 'external_photos', 'interior_photos')

    def get_external_photos(self, obj):
        external_photos = obj.external_photos.all()
        photos = [external.photo.url for external in external_photos]
        return photos

    def get_interior_photos(self, obj):
        interior_photos = obj.interior_photos.all()
        photos = [interior.photo.url for interior in interior_photos]
        return photos
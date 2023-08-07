from django.db import models
from parler.models import TranslatableModel, TranslatedFields

from apps.cars.models.review import CarReview


class SizeAndSpace(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
        dimensions_and_space = models.TextField()
    )
    height_width_photo = models.ImageField(upload_to="car-review/size-space/height-width-photo")
    length = models.ImageField(upload_to="car-review/size-space/length-photo")
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name='size_space')

    class Meta:
        db_table = "review_size_space"


class SizeAndSpacePhoto(models.Model):
    size_space = models.ForeignKey(SizeAndSpace, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="car-review/size-space/photos")

    class Meta:
        db_table = "review_size_space_photo"
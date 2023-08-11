from django.db import models
from .review import CarReview
from parler.models import TranslatableModel, TranslatedFields


class Design(TranslatableModel):
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="design")
    rated_by_orient_motors = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(upload_to="car-review/design")
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        external_design = models.TextField(),
        interior_design = models.TextField(),
        
    )

    class Meta:
        db_table = "review_design"


class ExternalDesignPhoto(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, related_name="external_photos")
    photo = models.ImageField(upload_to="car-review/design/external")

    class Meta:
        db_table = "review_external_disign_photo"


class InteriorDesignPhoto(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, related_name="interior_photos")
    photo = models.ImageField(upload_to="car-review/design/interior")

    class Meta:
        db_table = "review_interior_disign_photo"

    

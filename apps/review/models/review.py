from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class CarReview(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
        subtitle = models.CharField(max_length=200)
    )
    photo = models.ImageField(upload_to="car-review")

    class Meta:
        db_table = "review"



class SafetyAndConvenience(TranslatableModel):
    photo = models.ImageField(upload_to='car-review/safety_convenience')
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="safety_convenience")
    rated_by_orient_motors = models.PositiveSmallIntegerField(default=0)
    translations = TranslatedFields(
        safety_equipment = models.TextField(),
        convenience_equipment = models.TextField(),
    )

    class Meta:
        db_table = "review_safety_and_convenience"

    
class SafetyAndConvenienceAdvantages(TranslatableModel):
    translations = TranslatedFields(
        text = models.CharField(max_length=100)
    )
    safety_convenience = models.ForeignKey(SafetyAndConvenience, on_delete=models.CASCADE, related_name="advantages")

    class Meta:
        db_table = "review_safety_convenience_advantage"

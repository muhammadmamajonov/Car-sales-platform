from django.db import models
from parler.models import TranslatableModel, TranslatedFields

from apps.cars.models.review import CarReview


class Performance(TranslatableModel):
    photo = models.ImageField(upload_to='car-review/performance')
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE)
    rated_by_orient_motors = models.PositiveSmallIntegerField(default=0)
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
        direct_driving = models.TextField(),
        curved_driving = models.TextField(),
    )

    class Meta:
        db_table = "review_performance"


class PerformanceAdvantages(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )
    rated = models.PositiveSmallIntegerField(default=0)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name="advantages")

    class Meta:
        db_table = "review_performance_advantage"
    

class PerformanceFlaws(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )
    rated = models.PositiveSmallIntegerField(default=0)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name="flaws")

    class Meta:
        db_table = "review_performance_flaws"
    

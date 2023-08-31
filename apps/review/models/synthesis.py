from django.db import models
from .review import CarReview
from parler.models import TranslatableModel, TranslatedFields


class Synthesis(TranslatableModel):
    translations = TranslatedFields(
        text = models.TextField(),
        advantage = models.CharField(max_length=200),
        flaw = models.CharField(max_length=200),    
    )
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="synthesis")

    class Meta:
        db_table = "synthesis"


class CarReviewFAQ(TranslatableModel):
    translations = TranslatedFields(
        question = models.CharField(max_length=200),
        answer = models.TextField()
    )
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="faq")

    class Meta:
        db_table = "car_review_faq"
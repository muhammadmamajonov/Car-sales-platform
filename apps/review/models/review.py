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




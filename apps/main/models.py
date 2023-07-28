from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Region(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    class Meta:
        db_table = "region"
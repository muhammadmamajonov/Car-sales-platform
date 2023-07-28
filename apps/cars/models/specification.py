from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Fuel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "fuel"


class Transmission(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "transmission"
    
class Color(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    code = models.CharField(max_length=6)
    
    class Meta:
        db_table = "color"

    def __str__(self) -> str:
        return self.code
    


class BodyType(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=10)
    )

    class Meta:
        db_table = "body_type"
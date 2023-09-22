from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Fuel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "fuel"

    def __str__(self) -> str:
        return self.name
    

class Transmission(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "transmission"
    
    def __str__(self) -> str:
        return self.name


class Color(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    code = models.CharField(max_length=6)
    
    class Meta:
        db_table = "color"

    def __str__(self) -> str:
        return self.name
    

class PaintCondition(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )

    class Meta:
        db_table = "paint_condition"

    def __str__(self) -> str:
        return self.title
    

class BodyType(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=10)
    )

    class Meta:
        db_table = "body_type"

    def __str__(self) -> str:
        return self.name
    

class DriveUnit(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )

    class Meta:
        db_table = "drive_unit"
        
    def __str__(self) -> str:
        return self.title
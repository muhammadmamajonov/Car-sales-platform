from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class BodyType(models.Model):
    translations = TranslatedFields(
        name = models.CharField(max_length=10)
    )
    used = models.PositiveIntegerField(default=0)
    

class Service(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    used = models.PositiveIntegerField(default=0)
    

class Fuel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    used = models.PositiveIntegerField(default=0)
    

class Transmission(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    used = models.PositiveIntegerField(default=0)
    
    
class Color(TranslatableModel):
    translaations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    code = models.CharField(max_length=6)
    
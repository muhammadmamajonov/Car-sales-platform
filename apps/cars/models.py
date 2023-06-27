from django.db import models
from apps.users.models import User
from apps.main.models import Region
from parler.models import TranslatableModel, TranslatedFields


class BodyType(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=10)
    )
   

class Service(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    

class Fuel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    

class Transmission(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    
class Color(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    code = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return self.code

class Brand(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField()
    used = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    

class Model(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    used = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(help_text="Ishlab chiqarilgan yil")
    month = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Ishlab chiqarilgan oy")
    mileage = models.PositiveIntegerField(default=0)
    price = models.PositiveBigIntegerField()
    currency = models.CharField(max_length=4, choices=(('Usd', 'usd'), ('Uzs', 'uzs')), help_text="usd/uzs")
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    engine_size = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    liked_by = models.ManyToManyField(User, related_name="likes")
    rate = models.PositiveSmallIntegerField(default=0)
    owned_by_orient_motors = models.BooleanField(default=False)
    

from .brand import Model
from django.db import models
from .specification import *
from .service import Service
from apps.users.models import User
from apps.users.models import User
from apps.main.models import Region

class Car(models.Model):
    year = models.PositiveSmallIntegerField(help_text="Ishlab chiqarilgan yil")
    month = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Ishlab chiqarilgan oy")
    mileage = models.PositiveIntegerField(default=0)
    price = models.PositiveBigIntegerField()
    currency = models.CharField(max_length=4, choices=(('Usd', 'usd'), ('Uzs', 'uzs')), help_text="usd/uzs")
    engine_size = models.FloatField(default=0)
    horsepower = models.PositiveSmallIntegerField()
    used_car = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    liked_by = models.ManyToManyField(User, related_name="likes")
    rate = models.PositiveSmallIntegerField(default=0)
    owned_by_orient_motors = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "car"
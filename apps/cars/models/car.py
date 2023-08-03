from .brand import Model
from django.db import models
from apps.users.models import User
from apps.users.models import User
from apps.main.models import Region
from apps.specifications.models import BodyType, Color, Fuel, Transmission


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
    liked_by = models.ManyToManyField(User, related_name="likes", null=True, blank=True)
    rate = models.PositiveSmallIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    avtoritet_diagnostics = models.BooleanField()
    avtoritet_premium_diagnostics = models.BooleanField()
    orient_motors_warranty = models.BooleanField()
    owned_by_orient_motors = models.BooleanField(default=False)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "car"
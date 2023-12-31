from .brand import Model
from django.db import models
from apps.users.models import User
from apps.users.models import User
from apps.main.models import Region
from apps.specifications.models import (BodyType, Color, Fuel, Transmission, DriveUnit, Optics,
                                        PaintCondition, MediaTools, Salon, VehicleOptions, ExternalBodyKit)
    

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
    rated = models.PositiveSmallIntegerField(default=0)
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
    paint_condition = models.ManyToManyField(PaintCondition, related_name='cars')
    description = models.TextField()
    drive_unit = models.ForeignKey(DriveUnit, on_delete=models.SET_NULL, null=True, related_name='cars')
    number_of_owners = models.PositiveSmallIntegerField(default=1)
    media_tools = models.ManyToManyField(MediaTools, related_name='cars')
    optics = models.ManyToManyField(Optics, related_name='cars')
    external_body_kit = models.ManyToManyField(ExternalBodyKit, related_name='cars')
    salon = models.ManyToManyField(Salon, related_name='cars')
    vehicle_options = models.ManyToManyField(VehicleOptions, related_name='cars')
    

    class Meta:
        db_table = "car"

    
class CarPhotos(models.Model):
    photo = models.ImageField(upload_to="cars")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')



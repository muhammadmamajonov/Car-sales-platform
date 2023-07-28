from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField()
    used = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "brand"

    def __str__(self) -> str:
        return self.name
    

class Model(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    used = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "car_model"

    def __str__(self) -> str:
        return self.name
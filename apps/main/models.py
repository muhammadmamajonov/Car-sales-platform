from django.db import models
from apps.users.models import User
from parler.models import TranslatableModel, TranslatedFields


class Region(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    class Meta:
        db_table = "region"

    def __str__(self) -> str:
        return self.name
    

class Branch(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        address = models.CharField(max_length=255)
    )
    working_time = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    lat = models.FloatField()
    long = models.FloatField()


class BranchesPhoto(models.Model):
    photo = models.ImageField(upload_to="branches")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='photos')


class ComplaintToBranch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints_to_branches")
    text = models.TextField()


class SMSProvider(models.Model):
    token = models.TextField()

    
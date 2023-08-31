from .car import Car
from django.db import models
from apps.users.models import User
from parler.models import TranslatableModel, TranslatedFields


class Reason(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100)
    )

    class Meta:
        db_table = "complaint_reason"


class Complaints(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="complaints")
    complainant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, related_name="complaints")
    text = models.TextField()

    class Meta:
        db_table = "complaint"
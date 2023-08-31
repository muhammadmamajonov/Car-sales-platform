from django.db import models
from django.contrib.auth.models import AbstractUser
from parler.models import TranslatableModel, TranslatedFields


class SellersClassification(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100)
    )
    
    class Meta:
        db_table = "sellers_classification"


class User(AbstractUser):
    phone = models.CharField(max_length=17)
    sellertype = models.ForeignKey(SellersClassification, on_delete=models.SET_NULL, related_name="sellers", null=True, blank=True)
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    
    class Meta:
        db_table = "users"
        
    def __str__(self) -> str:
        return self.phone
    


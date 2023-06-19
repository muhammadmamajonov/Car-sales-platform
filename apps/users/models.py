from django.db import models
from django.contrib.auth.models import AbstractUser
from parler.models import TranslatableModel, TranslatedFields


class SellersClassification(models.Model):
    translations = TranslatedFields(
        name = models.CharField(max_length=100)
    )
    
    
class User(AbstractUser):
    phone = models.CharField(max_length=17)
    is_seller = models.BooleanField(default=False)
    sellertype = models.ForeignKey(SellersClassification, on_delete=models.SET_NULL, related_name="sellers", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.phone
    


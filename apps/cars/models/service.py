from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )

    class Meta:
        db_table = "service"
    

class ServiceInfo(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        description = models.TextField()
    )
    photo = models.ImageField(upload_to='service_info/photos')

    class Meta:
        db_table = "service_info"
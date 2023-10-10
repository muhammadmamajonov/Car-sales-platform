from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Fuel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "fuel"

    def __str__(self) -> str:
        return self.name
    

class Transmission(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "transmission"
    
    def __str__(self) -> str:
        return self.name


class Color(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50)
    )
    code = models.CharField(max_length=6)
    
    class Meta:
        db_table = "color"

    def __str__(self) -> str:
        return self.name
    

class PaintCondition(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )

    class Meta:
        db_table = "paint_condition"

    def __str__(self) -> str:
        return self.title
    

class BodyType(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=10)
    )

    class Meta:
        db_table = "body_type"

    def __str__(self) -> str:
        return self.name
    

class DriveUnit(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )

    class Meta:
        db_table = "drive_unit"
        
    def __str__(self) -> str:
        return self.title


class ExternalBodyKit(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )
    
    class Meta:
        db_table = "external_body_kit"
        
    def __str__(self):
        return self.title
    

class Optics(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "optics"

    def __str__(self):
        return self.title


class Salon(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "salon"
    
    def __str__(self):
        return self.title
    

class VehicleOptions(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "vehicle_options"
        
    def __str__(self):
        return self.title
    

class MediaTools(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=50)
    )
    
    class Meta:
        db_table = "media_tools"
    
    def __str__(self):
        return self.title
from django.db import models
from parler.models import TranslatableModel, TranslatedFields



class PremiumDiagnosticsInfo(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        description = models.TextField()
    )
    photo = models.ImageField(upload_to='premium_diagnostics/info')

    class Meta:
        db_table = "premium_diagnostics_info"
    

class PremiumDiagnosticsFAQ(TranslatableModel):
    translations = TranslatedFields(
       question = models.CharField(max_length=250),
       answer = models.TextField() 
    )

    class Meta:
        db_table = "premium_diagnostics_faq"


class SpecialDiagnosticEquipment(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
        description = models.TextField()
    )
    photo = models.ImageField(upload_to="premium_diagnostics/special_diagnostics")

    class Meta:
        db_table = 'special_diagnostic_equipment'

    
class DiagnosticSpecialists(TranslatableModel):
    translations = TranslatedFields(
        full_name = models.CharField(max_length=100),
        specialty = models.CharField(max_length=200)
    )
    experience = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to="premium-diagnostics/specialists")
    

class PremiumDiagnosticsHeader(TranslatableModel):
    translations = TranslatedFields(
        text = models.TextField(),
        sub_text = models.TextField()
    )
    video = models.FileField(upload_to='premium_dagnostics/header-video')
    
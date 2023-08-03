from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class DiagnosticsInfo(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        description = models.TextField()
    )
    photo = models.ImageField(upload_to='diagnostics/info')

    class Meta:
        db_table = "diagnostics_info"


class DiagnosticsFAQ(TranslatableModel):
    translations = TranslatedFields(
       question = models.CharField(max_length=250),
       answer = models.TextField() 
    )

    class Meta:
        db_table = "diagnostics_faq"
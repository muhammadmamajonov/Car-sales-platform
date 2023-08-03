from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models.diagnostics import DiagnosticsFAQ, DiagnosticsInfo
from .models.premium_diagnostics import DiagnosticSpecialists, PremiumDiagnosticsFAQ, PremiumDiagnosticsInfo, SpecialDiagnosticEquipment

@admin.register(DiagnosticsFAQ)
class DiagnosticsFAQAdmin(TranslatableAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id', 'question')


@admin.register(DiagnosticsInfo)
class DiagnosticsInfoAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


#premium

@admin.register(PremiumDiagnosticsInfo)
class PremiumDiagnosticsInfoAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(PremiumDiagnosticsFAQ)
class PremiumDiagnosticsFAQAdmin(TranslatableAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id', 'question')


@admin.register(SpecialDiagnosticEquipment)
class SpecialDiagnosticEquipmentAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(DiagnosticSpecialists)
class DiagnosticSpecialistsAdmin(TranslatableAdmin):
    list_display = ('id', 'full_name', 'specialty', 'experience')
    list_display_links = ('id', 'full_name', 'specialty')
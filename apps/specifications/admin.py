from django.contrib import admin
from .models import BodyType, Color, Fuel, Transmission
from parler.admin import TranslatableAdmin


class BodyTypeAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    fieldsets = (
        (None, {
            "fields":('name',)
        }),
    )
admin.site.register(BodyType, BodyTypeAdmin)


class ColorAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'code']
    fieldsets = (
        (None, {
            "fields":('name', 'code')
        }),
    )
admin.site.register(Color, ColorAdmin)



class FuelAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    fieldsets = (
        (None, {
            "fields":('name',)
        }),
    )
admin.site.register(Fuel, FuelAdmin)


class TransmissionAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    fieldsets = (
        (None, {
            "fields":('name',)
        }),
    )
admin.site.register(Transmission, TransmissionAdmin)
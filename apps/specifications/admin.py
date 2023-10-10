from django.contrib import admin
from .models import (BodyType, Color, Fuel, Transmission, PaintCondition, Optics, 
                     DriveUnit, MediaTools, VehicleOptions, ExternalBodyKit, Salon)
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


class PaintConditionAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
admin.site.register(PaintCondition, PaintConditionAdmin)


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


class DriveUnitAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
admin.site.register(DriveUnit, DriveUnitAdmin)


class MediaToolsAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
    
admin.site.register(MediaTools, MediaToolsAdmin)


class OpticsAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
    
admin.site.register(Optics, OpticsAdmin)


class VehicleOptionsAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
    
admin.site.register(VehicleOptions, VehicleOptionsAdmin)


class ExternalBodyKitAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
    
admin.site.register(ExternalBodyKit, ExternalBodyKitAdmin)


class SalonAdmin(TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            "fields":('title',)
        }),
    )
    
admin.site.register(Salon, SalonAdmin)
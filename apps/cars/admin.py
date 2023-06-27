from django.contrib import admin
from .models import *
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


class ServiceAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    fieldsets = (
        (None, {
            "fields":('name',)
        }),
    )
admin.site.register(Service, ServiceAdmin)


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


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon', 'used']
    fieldsets = (
        (None, {
            "fields":('name', 'icon')
        }),
    )
admin.site.register(Brand, BrandAdmin)


class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'used']
    fieldsets = (
        (None, {
            "fields":('name', 'brand')
        }),
    )
admin.site.register(Model, ModelAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'model', 'year', 'mileage', 'price', 'region']
    list_display_links = ['owner', 'model']
    
admin.site.register(Car, CarAdmin)

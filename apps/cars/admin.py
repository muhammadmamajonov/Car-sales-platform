from .models.brand import *
from .models.car import Car, CarPhotos
from django.contrib import admin



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
    list_display = ('id', 'owner', 'model', 'year', 'mileage', 'price', 'region')
    list_display_links = ['owner', 'model']
    
admin.site.register(Car, CarAdmin)

@admin.register(CarPhotos)
class CarPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')
    list_display_links = ('id', 'photo')


from django.contrib import admin
from .models import Region
from parler.admin import TranslatableAdmin


@admin.register(Region)
class RegionAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    fieldsets = (
        (None, {
            "fields":('name',)
        }),
    )

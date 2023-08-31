from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Region, Branch, BranchesPhoto, SMSProvider


@admin.register(Region)
class RegionAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    fieldsets = (
        (None, {
            "fields":('name',)
        }),
    )

@admin.register(Branch)
class BranchAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'address', 'working_time', 'address', 'lat', 'long')
    list_display_links = ('name', 'address')
    

@admin.register(BranchesPhoto)
class BranchPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')
    list_display_links = ('id', 'photo')

admin.site.register(SMSProvider)
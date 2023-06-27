from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('username', 'first_name')
    list_display = ('id', 'username', 'phone', 'first_name', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username')

   
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Ruxsatlar', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ("Shaxsiy ma'lumotlar", {'fields': ('phone', 'first_name', 'last_name')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', "is_staff", 'is_superuser')}
        ),
    )

admin.site.register(User, UserAdminConfig)
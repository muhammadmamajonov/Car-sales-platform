from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models.synthesis import Synthesis, CarReviewFAQ
from .models.size_and_space import SizeAndSpace, SizeAndSpacePhoto
from .models.review_design import Design, ExternalDesignPhoto, InteriorDesignPhoto
from .models.review import CarReview, SafetyAndConvenience, SafetyAndConvenienceAdvantages
from .models.review_performance import Performance, PerformanceAdvantages, PerformanceFlaws
from .models.maintenance_management import MaintenanceAndManagement, MaintenanceManagementAdvantages



@admin.register(CarReview)
class CarReviewAdmin(TranslatableAdmin):
    list_display = ('id', 'title', 'subtitle', 'photo')
    list_display_links = ('id', 'title', 'subtitle', 'photo')


@admin.register(Design)
class DesignAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')

admin.site.register(ExternalDesignPhoto)
admin.site.register(InteriorDesignPhoto)

@admin.register(Performance)
class PerformanceAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')

@admin.register(PerformanceAdvantages)
class PerformanceAdvantagesAdmin(TranslatableAdmin):
    list_display = ('id', 'performance', 'title', 'rated')
    list_display_links = ('id', 'performance', 'title')

@admin.register(PerformanceFlaws)
class PerformanceFlawsAdmin(TranslatableAdmin):
    list_display = ('id', 'performance', 'title', 'rated')
    list_display_links = ('id', 'performance', 'title')

@admin.register(SizeAndSpace)
class SizeAndSpaceAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')

admin.site.register(SizeAndSpacePhoto)

@admin.register(Synthesis)
class SynthesisAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review')
    list_display_links = ('id', 'car_review')

@admin.register(CarReviewFAQ)
class CarReviewFAQAdmin(TranslatableAdmin):
    list_display = ('id', 'question', 'answer', 'car_review')
    list_display_links = ('id', 'question', 'answer', 'car_review')

    
@admin.register(MaintenanceAndManagement)
class MaintenanceAndManagementAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')


@admin.register(MaintenanceManagementAdvantages)
class MaintenanceManagementAdvantagesAdmin(TranslatableAdmin):
    list_display = ('id', 'maintenance_management', 'text')
    list_display_links = ('id', 'maintenance_management', 'text')


@admin.register(SafetyAndConvenience)
class SafetyAndConvenienceAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'rated_by_orient_motors')
    list_display_links = ('id', 'car_review', 'rated_by_orient_motors')

@admin.register(SafetyAndConvenienceAdvantages)
class SafetyAndConvenienceAdvantagesAdmin(TranslatableAdmin):
    list_display = ('id', 'safety_convenience', 'text')
    list_display_links = ('id', 'safety_convenience', 'text')
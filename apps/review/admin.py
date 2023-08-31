from django.contrib import admin
from .models.review import CarReview
from .models.review_design import Design, ExternalDesignPhoto, InteriorDesignPhoto
from .models.review_performance import Performance, PerformanceAdvantages, PerformanceFlaws
from .models.size_and_space import SizeAndSpace
from .models.synthesis import Synthesis, CarReviewFAQ
from .models.maintenance_management import MaintenanceAndManagement, MaintenanceManagementAdvantages
from parler.admin import TranslatableAdmin


@admin.register(CarReview)
class CarReviewAdmin(TranslatableAdmin):
    list_display = ('id', 'title', 'subtitle', 'photo')
    list_display_links = ('id', 'title', 'subtitle', 'photo')


@admin.register(Design)
class DesignAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')


@admin.register(Performance)
class PerformanceAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')


@admin.register(SizeAndSpace)
class SizeAndSpaceAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')


@admin.register(Synthesis)
class SynthesisAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review')
    list_display_links = ('id', 'car_review')


@admin.register(MaintenanceAndManagement)
class MaintenanceAndManagementAdmin(TranslatableAdmin):
    list_display = ('id', 'car_review', 'title')
    list_display_links = ('id', 'car_review', 'title')
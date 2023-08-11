from django.db import models
from .review import CarReview
from parler.models import TranslatableModel, TranslatedFields


class MaintenanceAndManagement(TranslatableModel):
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="maintenance_management")
    rated_by_orient_motors = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(upload_to="car-review/maintenance_management")
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        fuel_efficiency = models.TextField(),
        Service = models.TextField(),
        warranty = models.TextField()
        
    )

    class Meta:
        db_table = "review_maintenance_management"

    

class MaintenanceManagementAdvantages(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100)
    )
    maintenance_management = models.ForeignKey(MaintenanceAndManagement, on_delete=models.CASCADE, related_name="advantages")

    class Meta:
        db_table = "review_maintenance_management_advantages"
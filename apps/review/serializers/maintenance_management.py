from ..models.maintenance_management import *
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework.serializers import SerializerMethodField


class MaintenanceManagementAdvantagesSerializer(TranslatableModelSerializer):
    class Meta:
        model = MaintenanceManagementAdvantages
        fields = ('title', )


class MaintenanceManagementSerializer(TranslatableModelSerializer):
    advantages = SerializerMethodField()
    class Meta:
        model = MaintenanceAndManagement
        fields = ('title', 'service', 'warranty', 'rated_by_orient_motors', 'fuel_efficiency', 'photo', 'advantages')

    def get_advantages(self, obj):
        advantages = MaintenanceManagementAdvantagesSerializer(obj.advantages.all()).data
        return advantages
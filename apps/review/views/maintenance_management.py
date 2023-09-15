from rest_framework.generics import RetrieveAPIView
from ..models.maintenance_management import MaintenanceAndManagement
from ..serializers.maintenance_management import MaintenanceManagementSerializer


class MaintenanceAndManagementAPIView(RetrieveAPIView):
    serializer_class = MaintenanceManagementSerializer
    queryset = MaintenanceAndManagement
    lookup_field = 'car_review_id'
    authentication_classes = []
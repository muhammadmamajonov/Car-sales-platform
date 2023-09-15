from ..models.review_performance import Performance
from rest_framework.generics import RetrieveAPIView
from ..serializers.review_performance import PerformanceSerializer


class ReviewPerformanceAPIView(RetrieveAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    lookup_field = 'car_review_id'
    authentication_classes = []
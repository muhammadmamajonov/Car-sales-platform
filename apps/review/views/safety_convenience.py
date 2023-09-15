from ..models.review import SafetyAndConvenience
from rest_framework.generics import RetrieveAPIView
from ..serializers.safety_convenience import SafetyConvenienceGetSerializer
from django.utils.translation import get_language_from_request

class SafetyConvenienceGetAPIView(RetrieveAPIView):
    # queryset = SafetyAndConvenience.objects.all()
    serializer_class = SafetyConvenienceGetSerializer
    lookup_field = 'car_review_id'
    authentication_classes = []

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = SafetyAndConvenience.objects.language(language).all()
        return super().get_queryset()
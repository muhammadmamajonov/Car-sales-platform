from ..models import PaintCondition
from rest_framework.generics import ListAPIView
from django.utils.translation import get_language_from_request
from ..serializers.paint_condition import PaintConditionListSerializer



class PaintConditionListAPIView(ListAPIView):
    serializer_class = PaintConditionListSerializer

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = PaintCondition.objects.language(language).all()
        return super().get_queryset()
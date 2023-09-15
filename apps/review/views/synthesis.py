from rest_framework.generics import RetrieveAPIView
from ..models.synthesis import Synthesis, CarReviewFAQ
from ..serializers.synthesis import SynthesisGetSerializer, CarReviewFAQGetSerializer



class SynthesisGetAPIView(RetrieveAPIView):
    queryset = Synthesis.objects.all()
    serializer_class = SynthesisGetSerializer
    lookup_field = 'car_review_id'
    authentication_classes = []


class CarReviewFAQGetAPIView(RetrieveAPIView):
    queryset = CarReviewFAQ.objects.all()
    serializer_class = CarReviewFAQGetSerializer
    lookup_field = 'car_review_id'
    authentication_classes = []
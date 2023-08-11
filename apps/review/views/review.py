from ..models.review import CarReview
from rest_framework.generics import ListAPIView
from ..serializers.review import CarReviewListSerializer


class CarReviewListAPIView(ListAPIView):
    serializer_class = CarReviewListSerializer
    queryset = CarReview.objects.all()
    authentication_classes = []
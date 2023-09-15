from ..models.review_design import Design
from ..serializers.review_design import ReviewDesignSerializer
from rest_framework.generics import RetrieveAPIView


class ReviewDesignAPIView(RetrieveAPIView):
    serializer_class = ReviewDesignSerializer
    queryset = Design.objects.all()
    lookup_field = 'car_review_id'
    authentication_classes = []
from ..models.size_and_space import SizeAndSpace
from ..serializers.size_space import SizeSpaceGetSerializer
from rest_framework.generics import RetrieveAPIView


class SizeSpaceGetAPIView(RetrieveAPIView):
    serializer_class = SizeSpaceGetSerializer
    queryset = SizeAndSpace.objects.all()
    lookup_field = 'car_review_id'
    authentication_classes = []
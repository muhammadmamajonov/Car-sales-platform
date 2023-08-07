from ..models.brand import Brand, Model
from rest_framework.permissions import IsAdminUser
from ..serializers.brand import BrandSerializer, CarModelSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView



class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]


class BrandEditAPIView(UpdateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAdminUser]
    http_method_names = ['patch']


class BrandListAPIView(ListAPIView):
    authentication_classes = []
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ModelCreateAPIView(CreateAPIView):
    serializer_class = CarModelSerializer
    permission_classes = [IsAdminUser]


class ModelEditAPIView(UpdateAPIView):
    serializer_class = CarModelSerializer
    queryset = Model.objects.all()
    permission_classes = [IsAdminUser]
    http_method_names = ['patch']


class ModelListAPIView(ListAPIView):
    """/car/model/list?brand_id=brand_id shu ko'rinishda brand idsi yuboriladi"""
    authentication_classes = []
    serializer_class = CarModelSerializer

    def get_queryset(self):
        brand_id = self.request.GET.get('brand_id')
        self.queryset = Model.objects.filter(brand_id=brand_id)
        return super().get_queryset()




from ..models.brand import Brand, Model
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from ..serializers.brand import BrandSerializer, CarModelSerializer, FilterModelSerializer, FilterBrandSerializer


authentication_classes = [SessionAuthentication, JWTAuthentication]

class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes


class BrandEditAPIView(UpdateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ModelCreateAPIView(CreateAPIView):
    serializer_class = CarModelSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes


class ModelEditAPIView(UpdateAPIView):
    serializer_class = CarModelSerializer
    queryset = Model.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class ModelListAPIView(ListAPIView):
    """/car/model/list?brand_id=brand_id shu ko'rinishda brand idsi yuboriladi"""
    serializer_class = CarModelSerializer

    def get_queryset(self):
        brand_id = self.request.GET.get('brand_id')
        self.queryset = Model.objects.filter(brand_id=brand_id)
        return super().get_queryset()


class FilterBrandAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = FilterBrandSerializer

    def list(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        serializer = self.serializer_class(brands, many=True)
        sorted_brands = sorted(serializer.data, key=lambda brand: brand['count'], reverse=True)
        print(sorted_brands)
        return Response(sorted_brands)


class FilterModelAPIView(ListAPIView):
    serializer_class = FilterModelSerializer
    queryset = Model.objects.all()

    def get_queryset(self):
        brand_id = self.request.GET.get('brand_id')
        self.queryset = Model.objects.filter(brand_id=brand_id)
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        brands = self.get_queryset()
        serializer = self.serializer_class(brands, many=True)
        sorted_brands = sorted(serializer.data, key=lambda brand: brand['count'], reverse=True)
        return Response(sorted_brands)

from rest_framework.response import Response
from apps.cars.models.brand import Brand, Model
from rest_framework.generics import ListAPIView
from apps.cars.serializers.brand import FilterModelSerializer, FilterBrandSerializer



class FilterBrandAPIView(ListAPIView):
    authentication_classes = []
    queryset = Brand.objects.all()
    serializer_class = FilterBrandSerializer

    def list(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        serializer = self.serializer_class(brands, many=True)
        sorted_brands = sorted(serializer.data, key=lambda brand: brand['count'], reverse=True)
        print(sorted_brands)
        return Response(sorted_brands)


class FilterModelAPIView(ListAPIView):
    authentication_classes = []
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
from apps.cars.models import BodyType, Car
from rest_framework.response import Response
from ..schemas import body_type_with_count_schema
from rest_framework.permissions import IsAdminUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.body_type import BodyTypeListSerializer, BodyTypeSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

authentication_classes = [SessionAuthentication, JWTAuthentication]


class BodyTypeCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BodyTypeSerializer
    authentication_classes = authentication_classes



class BodyTypeEditAPIView(UpdateAPIView):
    http_method_names = ['patch']
    queryset = BodyType.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = BodyTypeSerializer
    authentication_classes = authentication_classes


class BodyTypeDetailAPIView(RetrieveAPIView):
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeSerializer


class BodyTypeListAPIView(ListAPIView):
    serializer_class = BodyTypeListSerializer

    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = BodyType.objects.language(language).all()
        return super().get_queryset()
    

class BodyTypeWithCountAPIView(ListAPIView):
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeListSerializer
    schema = body_type_with_count_schema

    def list(self, request, *args, **kwargs):
        query = {}
        model_id = request.GET.get('model_id')
        print(model_id)
        min_year = request.GET.get('min_year')
        max_year = request.GET.get('max_year')
        min_month = request.GET.get('min_month')
        max_month = request.GET.get('max_month')
        min_mileage = request.GET.get('min_mileage')
        max_mileage = request.GET.get('max_mileage')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        currency = request.GET.get('currency')

        if model_id:
            query['model_id']=model_id
        if min_year:
            query['year__gte']=min_year
        if max_year:
            query['year__lte']=max_year
        if min_month:
            query['month__gte']=min_month
        if max_month:
            query['month__lte']=max_month
        if min_mileage:
            query['mileage__gte']=min_mileage
        if max_mileage:
            query['mileage__lte']=max_mileage
        if min_price:
            query['price__gte']=min_price
        if max_price:
            query['price__lte']=max_price
        if currency:
            query['currency']=currency
    
        serialized = self.serializer_class(self.get_queryset(), many=True, context={'request':request}).data

        for i in range(len(serialized)):
            count = Car.objects.filter(body_type_id=serialized[i]['id'], **query).count()
            serialized[i]['count']=count
        
        sorted_data = sorted(serialized, key=lambda data: data['count'], reverse=True)
        return Response(sorted_data)
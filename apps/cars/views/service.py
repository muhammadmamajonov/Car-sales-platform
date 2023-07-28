from ..models.car import Car
from ..models.service import Service
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.utils.translation import get_language_from_request
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.service import ServiceListSerializer, ServiceSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

authentication_classes = [SessionAuthentication, JWTAuthentication]


class ServiceCreateAPIView(CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes


class ServiceEditAPIView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch']


class ServiceGetAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceListSerializer
    
    def get_queryset(self):
        language = get_language_from_request(self.request)
        self.queryset = Service.objects.language(language).all()
        return super().get_queryset()


class Old3ServiesListAPIView(ListAPIView):
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()[:3]


class ServiceWithCountAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        query = {}
        model_id = request.GET.get('model_id')
        min_year = request.GET.get('min_year')
        max_year = request.GET.get('max_year')
        min_month = request.GET.get('min_month')
        max_month = request.GET.get('max_month')
        min_mileage = request.GET.get('min_mileage')
        max_mileage = request.GET.get('max_mileage')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        currency = request.GET.get('currency')
        body_type = request.GET.get('body_type')
        fuel = request.GET.get('fuel')

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
        if body_type:
            query['body_type']=body_type
        if fuel:
            query['fuel']=fuel

        
        serialized = self.serializer_class(self.get_queryset(), many=True, context={'request':request}).data

        for i in range(len(serialized)):
            count = Car.objects.filter(body_type_id=serialized[i]['id'], **query).count()
            serialized[i]['count']=count
        
        sorted_data = sorted(serialized, key=lambda data: data['count'], reverse=True)
        return Response(sorted_data)
    
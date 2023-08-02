from apps.cars.models.car import Car
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from apps.specifications.models import Transmission
from apps.specifications.serializers.transmission import *


class TransmissionListWithCountAPIView(ListAPIView):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer

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
            service = request.GET.get('service')
            fuel = request.GET.get('fuel')
            color = request.GET.get('color')


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
                query['body_type_id']=body_type
            if service:
                query['service_id']=service
            if fuel:
                query['fuel_id']=fuel
            if color:
                query['color_id']=color
                

            serialized = self.serializer_class(self.get_queryset(), many=True, context={'request':request}).data

            for i in range(len(serialized)):
                count = Car.objects.filter(body_type_id=serialized[i]['id'], **query).count()
                serialized[i]['count']=count
            
            sorted_data = sorted(serialized, key=lambda data: data['count'], reverse=True)
            return Response(sorted_data)
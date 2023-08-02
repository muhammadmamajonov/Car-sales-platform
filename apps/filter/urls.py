from django.urls import path
from .views.colors_list_with_count import *
from .views.services_list_with_count import *
from .views.body_type_list_with_count import *
from .views.transmission_list_with_count import *
from .views.brand_model_list_with_count import *


urlpatterns = [
    path('model/', FilterModelAPIView.as_view()),
    path('brands/', FilterBrandAPIView.as_view()),
    path('color/', ColorListWithCountAPIView.as_view()),
    path('service/', ServiceWithCountAPIView.as_view()),
    path('body-type/', BodyTypeWithCountAPIView.as_view()),
    path('transmission/', TransmissionListWithCountAPIView.as_view()),
]
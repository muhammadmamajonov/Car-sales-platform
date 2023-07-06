from .views.car import *
from .views.fuel import *
from .views.brand import *
from .views.color import *
from .views.service import *
from .views.body_type import *
from .views.transmission import *
from django.urls import path

urlpatterns = [
    path('post', CarPostAPIView.as_view()),
    path('get/<int:pk>', CarGetAPIView.as_view()),
    path('edit/<int:pk>', CarEditAPIView.as_view()),
    path('list', CarListAPIView.as_view()),
    path('list/owned-by-orient-motors', CarsOwnedByOrientMotorsAPIView.as_view()),

    path('brand/add', BrandCreateView.as_view()),
    path('brand/list', BrandListAPIView.as_view()),
    path('brand/edit/<int:pk>', BrandEditAPIView.as_view()),

    path('model/add', ModelCreateAPIView.as_view()),
    path('model/list', ModelListAPIView.as_view()),
    path('model/edit/<int:pk>', ModelEditAPIView.as_view()),

    path('body-type/list', BodyTypeListAPIView.as_view()),
    path('body-type/add', BodyTypeCreateAPIView.as_view()),
    path('body-type/edit/<int:pk>', BodyTypeEditAPIView.as_view()),
    path('body-type/get/<int:pk>', BodyTypeDetailAPIView.as_view()),

    path('color/list', ColorListAPIView.as_view()),
    path('color/add', ColorCreateAPIView.as_view()),
    path('color/get/<int:pk>', ColorGetAPIView.as_view()),
    path('color/edit/<int:pk>', ColorEditAPIView.as_view()),

    path('fuel/list', FuelListAPIView.as_view()),
    path('fuel/add', FuelCreateAPIView.as_view()),
    path('fuel/get/<int:pk>', FuelGetAPIView.as_view()),
    path('fuel/edit/<int:pk>', FuelEditAPIView.as_view()),

    path('service/list', ServiceListAPIView.as_view()),
    path('service/add', ServiceCreateAPIView.as_view()),
    path('service/get/<int:pk>', ServiceGetAPIView.as_view()),
    path('service/edit/<int:pk>', ServiceEditAPIView.as_view()),

    path('transmission/list', TransmissionListAPIView.as_view()),
    path('transmission/add', TransmissionCreateAPIView.as_view()),
    path('transmission/get/<int:pk>', TransmissionGetAPIView.as_view()),
    path('transmission/edit/<int:pk>', TransmissionEditAPIView.as_view()),

    path('filter/model', FilterModelAPIView.as_view()),
    path('filter/brands', FilterBrandAPIView.as_view()),
    path('filter/body-type', BodyTypeWithCountAPIView.as_view()),
    path('filter/service', ServiceWithCountAPIView.as_view()),
    path('filter/transmission', TransmissionListWithCountAPIView.as_view()),
]
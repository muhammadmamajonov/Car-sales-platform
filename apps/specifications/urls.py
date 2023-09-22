from django.urls import path
from .views.drive_unit import DriveUnitListAPIView
from .views.paint_condition import PaintConditionListAPIView
from .views.fuel import FuelAddAPIView, FuelListAPIView, FuelRetrieveUpdateAPIView
from .views.color import ColorAddAPIView, ColorListAPIView, ColorRetrieveUpdateAPIView
from .views.body_type import BodyTypeAddAPIView, BodyTypeListAPIView, BodyTypeRetieveUpdateAPIView
from .views.transmission import TransmissionAddAPIView, TransmissionRetrieveUpdateAPIView, TransmissionsListAPIView


urlpatterns = [
    path('fuel/add/', FuelAddAPIView.as_view()),
    path('fuel/<int:pk>/', FuelRetrieveUpdateAPIView.as_view()),
    path('fuel/list/', FuelListAPIView.as_view()),

    path('color/add/', ColorAddAPIView.as_view()),
    path('color/<int:pk>/', ColorRetrieveUpdateAPIView.as_view()),
    path('color/list/', ColorListAPIView.as_view()),

    path('body-type/add/', BodyTypeAddAPIView.as_view()),
    path('body-type/<int:pk>/', BodyTypeRetieveUpdateAPIView.as_view()),
    path('body-type/list/', BodyTypeListAPIView.as_view()),

    path('transmission/add/', TransmissionAddAPIView.as_view()),
    path('transmission/<int:pk>/', TransmissionRetrieveUpdateAPIView.as_view()),
    path('transmission/list/', TransmissionsListAPIView.as_view()),

    path('drive-unit/list/',  DriveUnitListAPIView.as_view()),
    path('paint-condition/list/', PaintConditionListAPIView.as_view())
]
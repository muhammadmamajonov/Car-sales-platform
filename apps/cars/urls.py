from .views.car import *
from .views.brand import *
from .views.complaint import *
from django.urls import path

urlpatterns = [
    path('post/', CarPostAPIView.as_view()),
    path('get/<int:pk>/', CarGetAPIView.as_view()),
    path('edit/<int:pk>/', CarEditAPIView.as_view()),
    path('list/', CarListAPIView.as_view()),
    path('owned-by-orient-motors/', CarsOwnedByOrientMotorsAPIView.as_view()),
    path('diagnosed-cars/', DiagnosedCarsListAPIView.as_view()),
    path('premium-diagnosed-cars/', PremiumDiagnosedCarsListAPIView.as_view()),
    path('like/<int:car_id>/', LikeAPIView.as_view()),

    path('brand/add/', BrandCreateView.as_view()),
    path('brand/list/', BrandListAPIView.as_view()),
    path('brand/edit/<int:pk>/', BrandEditAPIView.as_view()),

    path('model/add/', ModelCreateAPIView.as_view()),
    path('model/list/', ModelListAPIView.as_view()),
    path('model/edit/<int:pk>/', ModelEditAPIView.as_view()),

    path('complaint/reasons/', ReasonsListAPIView.as_view()),
    path('complaint/post/', ComplaintPostAPIView.as_view())

]
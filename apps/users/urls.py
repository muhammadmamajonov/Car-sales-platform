from django.urls import path
from .views.authentication import *


urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('verification-code/send/', SendOTPAPIView.as_view()),
    path('verification-code/verify/', VerifyOTPAPIView.as_view()),
    path('registration/', UserRegistrationAPIView.as_view())
]
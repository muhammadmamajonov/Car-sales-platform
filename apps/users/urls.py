from django.urls import path
from .views.authentication import LoginAPIView


urlpatterns = [
    path('login', LoginAPIView.as_view())
]
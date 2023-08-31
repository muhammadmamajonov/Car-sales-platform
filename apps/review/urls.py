from django.urls import path
from .views.review import CarReviewListAPIView


urlpatterns = [
    path('list', CarReviewListAPIView.as_view()),
]
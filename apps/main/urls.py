from django.urls import path
from .views.branch import *


urlpatterns = [
    path('branch/', BranchAddAPIView.as_view()),
    path('branch/<int:pk>/', BranchRetrieveUpdateAPIView.as_view()),
    path('branch/list/', BranchesListAPIView.as_view()),
    path('branch/complaint/post/', ComplaintToBranchPostAPIView.as_view())
]
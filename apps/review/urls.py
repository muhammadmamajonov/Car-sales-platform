from django.urls import path
from .views.review import CarReviewListAPIView
from .views.size_space import SizeSpaceGetAPIView
from .views.review_design import ReviewDesignAPIView
from .views.review_performance import ReviewPerformanceAPIView
from .views.safety_convenience import SafetyConvenienceGetAPIView
from .views.synthesis import SynthesisGetAPIView, CarReviewFAQGetAPIView
from .views.maintenance_management import MaintenanceAndManagementAPIView


urlpatterns = [
    path('list/', CarReviewListAPIView.as_view()),
    path('maintenance-management/<int:car_review_id>/', MaintenanceAndManagementAPIView.as_view()),
    path('design/<int:car_review_id>/', ReviewDesignAPIView.as_view()),
    path('performance/<int:car_review_id>/', ReviewPerformanceAPIView.as_view()),
    path('size-space/<int:car_review_id>/', SizeSpaceGetAPIView.as_view()),
    path('systhesis/<int:car_review_id>/', SynthesisGetAPIView.as_view()),
    path('faq/<int:car_review_id>/', CarReviewFAQGetAPIView.as_view()),
    path('safety-convenience/<int:car_review_id>/', SafetyConvenienceGetAPIView.as_view())
]
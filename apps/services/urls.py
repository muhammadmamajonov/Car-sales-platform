from django.urls import path 
from .views.diagnostics import *
from .views.premium_diagnostics import *

urlpatterns = [
    path('diagnostics/info/', DiagnosticsInfoCreateAPIView.as_view()),
    path('diagnostics/info/<int:pk>/', DiagnosticsInfoRetrieveEditAPIView.as_view()),
    path('diagnostics/info/list/', DiagnosticsInfoListAPIView.as_view()),

    path('premium-diagnostics/info/', PremiumDiagnosticsInfoCreateAPIView.as_view()),
    path('premium-diagnostics/info/<int:pk>/', PremiumDiagnosticsInfoRetrieveEditAPIView.as_view()),
    path('premium-diagnostics/info/list/', PremiumDiagnosticsInfoListAPIView.as_view()),
    path('premium-diagnostics/special-diagnostic-equipent/', SpecialDiagnosticEquipentAddAPIView.as_view()),
    path('premium-diagnostics/special-diagnostic-equipent/<int:pk>/', SpecialDiagnosticEquipentRetrieveUpdateAPIViewAPIView.as_view()),
    path('premium-diagnostics/special-diagnostic-equipent/list/', SpecialDiagnosticEquipentListAPIView.as_view()),
    path('premium-diagnostics/specialists/', DiagnosticSpecialistsAddAPIView.as_view()),
    path('premium-diagnostics/specialists/<int:pk>/', DiagnosticSpecialistsRetrieveUpdateAPIView.as_view()),
    path('premium-diagnostics/specialists/list/', DiagnosticSpecialistsListAPIView.as_view())


]
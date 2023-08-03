from utils.permissions import IsSuperUser
from ..serializers.premium_diagnostics import *
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from ..models.premium_diagnostics import PremiumDiagnosticsFAQ, PremiumDiagnosticsInfo, SpecialDiagnosticEquipment

authentication_classes = [SessionAuthentication, JWTAuthentication]


class PremiumDiagnosticsInfoCreateAPIView(CreateAPIView):
    serializer_class = PremiumDiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes


class PremiumDiagnosticsInfoRetrieveEditAPIView(RetrieveUpdateAPIView):
    queryset = PremiumDiagnosticsInfo.objects.all()
    serializer_class = PremiumDiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch', 'get']



class PremiumDiagnosticsInfoListAPIView(ListAPIView):
    serializer_class = PremiumDiagnosticsInfoListSerializer
    queryset = PremiumDiagnosticsInfo.objects.all()


## FAQ

class PremiumDiagnosticsFAQCreateAPIView(CreateAPIView):
    serializer_class = PremiumDiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes


class PremiumDiagnosticsFAQRetrieveEditAPIView(RetrieveUpdateAPIView):
    serializer_class = PremiumDiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch', 'get']


class PremiumDiagnosticsFAQListAPIView(ListAPIView):
    serializer_class = PremiumDiagnosticsFAQListSerializer
    queryset = PremiumDiagnosticsFAQ.objects.all()


# Special diagnostics Equipent

class SpecialDiagnosticEquipentAddAPIView(CreateAPIView):
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes
    serializer_class = SpecialDiagnosticEquipmentSerializer


class SpecialDiagnosticEquipentRetrieveUpdateAPIViewAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes
    queryset = SpecialDiagnosticEquipment.objects.all()
    serializer_class = SpecialDiagnosticEquipmentSerializer
    http_method_names = ('patch', 'get')


class SpecialDiagnosticEquipentListAPIView(ListAPIView):
    queryset = SpecialDiagnosticEquipment.objects.all()
    serializer_class = SpecialDiagnosticEquipmentListSerializer


# Diagnostic Specialists

class DiagnosticSpecialistsAddAPIView(CreateAPIView):
    serializer_class = DiagnosticSpecialistsSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes


class DiagnosticSpecialistsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = DiagnosticSpecialists.objects.all()
    serializer_class = DiagnosticSpecialistsSerializer
    permission_classes = (IsSuperUser,)
    authentication_classes = authentication_classes
    http_method_names = ('patch', 'get')


class DiagnosticSpecialistsListAPIView(ListAPIView):
    queryset = DiagnosticSpecialists.objects.all()
    serializer_class = DiagnosticSpecialistsListSerializer


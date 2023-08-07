from rest_framework.views import APIView
from utils.permissions import IsSuperUser
from rest_framework.response import Response
from ..serializers.premium_diagnostics import *
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from ..models.premium_diagnostics import PremiumDiagnosticsFAQ, PremiumDiagnosticsHeader, PremiumDiagnosticsInfo, SpecialDiagnosticEquipment





class PremiumDiagnosticsInfoCreateAPIView(CreateAPIView):
    serializer_class = PremiumDiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]


class PremiumDiagnosticsInfoRetrieveEditAPIView(RetrieveUpdateAPIView):
    queryset = PremiumDiagnosticsInfo.objects.all()
    serializer_class = PremiumDiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]
    http_method_names = ['patch', 'get']



class PremiumDiagnosticsInfoListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = PremiumDiagnosticsInfoListSerializer
    queryset = PremiumDiagnosticsInfo.objects.all()


## FAQ

class PremiumDiagnosticsFAQCreateAPIView(CreateAPIView):
    serializer_class = PremiumDiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]


class PremiumDiagnosticsFAQRetrieveEditAPIView(RetrieveUpdateAPIView):
    serializer_class = PremiumDiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]
    http_method_names = ['patch', 'get']


class PremiumDiagnosticsFAQListAPIView(ListAPIView):
    authentication_classes = []
    serializer_class = PremiumDiagnosticsFAQListSerializer
    queryset = PremiumDiagnosticsFAQ.objects.all()


# Special diagnostics Equipent

class SpecialDiagnosticEquipentAddAPIView(CreateAPIView):
    permission_classes = (IsSuperUser,)
    serializer_class = SpecialDiagnosticEquipmentSerializer


class SpecialDiagnosticEquipentRetrieveUpdateAPIViewAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsSuperUser,)
    queryset = SpecialDiagnosticEquipment.objects.all()
    serializer_class = SpecialDiagnosticEquipmentSerializer
    http_method_names = ('patch', 'get')


class SpecialDiagnosticEquipentListAPIView(ListAPIView):
    authentication_classes = []
    queryset = SpecialDiagnosticEquipment.objects.all()
    serializer_class = SpecialDiagnosticEquipmentListSerializer


# Diagnostic Specialists

class DiagnosticSpecialistsAddAPIView(CreateAPIView):
    serializer_class = DiagnosticSpecialistsSerializer
    permission_classes = (IsSuperUser,)


class DiagnosticSpecialistsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = DiagnosticSpecialists.objects.all()
    serializer_class = DiagnosticSpecialistsSerializer
    permission_classes = (IsSuperUser,)
    http_method_names = ('patch', 'get')


class DiagnosticSpecialistsListAPIView(ListAPIView):
    authentication_classes = []
    queryset = DiagnosticSpecialists.objects.all()
    serializer_class = DiagnosticSpecialistsListSerializer


class PremiumDiagnosticsHeaderAPIView(APIView):
    authentication_classes = []

    def get(self, request):
        header = PremiumDiagnosticsHeader.objects.first()
        data = PremiumDiagnosticsHeaderSerializer(header, context={'request':request}).data
        return Response(data)


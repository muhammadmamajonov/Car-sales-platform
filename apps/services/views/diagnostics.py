from utils.permissions import IsSuperUser
from ..serializers.diagnostics import *
from ..models.diagnostics import DiagnosticsFAQ, DiagnosticsInfo
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView



class DiagnosticsInfoCreateAPIView(CreateAPIView):
    serializer_class = DiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]


class DiagnosticsInfoRetrieveEditAPIView(RetrieveUpdateAPIView):
    queryset = DiagnosticsInfo.objects.all()
    serializer_class = DiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]
    http_method_names = ['patch', 'get']



class DiagnosticsInfoListAPIView(ListAPIView):
    serializer_class = DiagnosticsInfoListSerializer
    queryset = DiagnosticsInfo.objects.all()
    authentication_classes = []



## FAQ

class DiagnosticsFAQCreateAPIView(CreateAPIView):
    serializer_class = DiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]


class DiagnosticsFAQRetrieveEditAPIView(RetrieveUpdateAPIView):
    serializer_class = DiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]


class DiagnosticsFAQListAPIView(ListAPIView):
    serializer_class = DiagnosticsFAQListSerializer
    queryset = DiagnosticsFAQ.objects.all()
    authentication_classes = []
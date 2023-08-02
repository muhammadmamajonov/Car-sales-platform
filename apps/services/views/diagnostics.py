from utils.permissions import IsSuperUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.diagnostics import *
from ..models.diagnostics import DiagnosticsFAQ, DiagnosticsInfo
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView

authentication_classes = [SessionAuthentication, JWTAuthentication]


class DiagnosticsInfoCreateAPIView(CreateAPIView):
    serializer_class = DiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes


class DiagnosticsInfoRetrieveEditAPIView(RetrieveUpdateAPIView):
    queryset = DiagnosticsInfo.objects.all()
    serializer_class = DiagnosticsInfoSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes
    http_method_names = ['patch', 'get']



class DiagnosticsInfoListAPIView(ListAPIView):
    serializer_class = DiagnosticsInfoListSerializer
    queryset = DiagnosticsInfo.objects.all()



## FAQ

class DiagnosticsFAQCreateAPIView(CreateAPIView):
    serializer_class = DiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes


class DiagnosticsFAQRetrieveEditAPIView(RetrieveUpdateAPIView):
    serializer_class = DiagnosticsFAQSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = authentication_classes


class DiagnosticsFAQListAPIView(ListAPIView):
    serializer_class = DiagnosticsFAQListSerializer
    queryset = DiagnosticsFAQ.objects.all()
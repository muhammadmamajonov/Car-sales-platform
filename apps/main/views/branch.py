from ..models import Branch
from utils.permissions import IsSuperUser
from ..serializers.branch import BranchSerializer, BranchListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView


class BranchAddAPIView(CreateAPIView):
    permission_classes = IsSuperUser
    serializer_class = BranchSerializer


class BranchRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = IsSuperUser
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    http_method_names = ('patch', 'get')


class BranchesListAPIView(ListAPIView):
    serializer_class = BranchListSerializer
    queryset = Branch.objects.all()
    authentication_classes = []





from ..models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token, RefreshToken, AccessToken


class LoginAPIView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        user = User.objects.filter(phone=phone).first()
        if not user:
            user = User.objects.create(phone=phone)
        refresh = RefreshToken.for_user(user)
        return Response({"access":str(refresh.access_token), "refresh":str(refresh)})
        
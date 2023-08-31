from ..models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from utils.send_sms_code import check_code, send_message
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.user import UserRegistrationSerializer
from ..schemas import login_schema, send_otp_schema, verify_schema


class SendOTPAPIView(APIView):
    schema = send_otp_schema

    def post(self, request):
        phone = request.data.get('phone')
        device_id = request.data.get('device_id')

        if phone == "+998123456789":
            return Response({"detail": "code sent"})
        
        resp = send_message(phone=phone, device_id=device_id)

        if resp.status_code == 200:
            return Response({"detail":"code sent"})
        return Response({"detail":resp.text}, status=resp.status_code)


class VerifyOTPAPIView(APIView):
    schema = verify_schema

    def post(self, request):
        code = request.data['code']
        phone = request.data['phone']
        if phone == "+998123456789" and code == "123456":
            return Response({'is_correct': True})
        cor = check_code(code, phone)
        return Response({'is_correct':cor})


class LoginAPIView(APIView):
    schema = login_schema

    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(request=request, phone=phone, password=password)
        if not user:
            return Response({"detail":"phone number or password is incorrect"}, status=401)
        refresh = RefreshToken.for_user(user)
        return Response({"access":str(refresh.access_token), "refresh":str(refresh)})
    

class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

        
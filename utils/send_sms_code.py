import os
import json
import requests
import redis
import math, random
from apps.main.models import SMSProvider


BASE_URL = "https://notify.eskiz.uz/api"
rds = redis.Redis(host='localhost', port=6379, db=0)


# function to generate OTP
def generateOTP(phone):
    digits = "0123456789"
    OTP = ""

    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    rds.set(name=phone, value=OTP)
    rds.expire(name=phone, time=65)

    return OTP

def check_code(code, phone):
    orginal_code = rds.get(phone)
    if orginal_code is None:
        return False
    orginal_code=orginal_code.decode('utf-8')
    correct = orginal_code == code
    return correct


def refresh_token():
    url = BASE_URL + "/auth/login"

    payload={
        'email': os.getenv("ESKIZ_EMAIL"),
        'password': os.getenv("ESKIZ_PASSWORD")
    }

    response = requests.request("POST", url, data=payload)
    data = json.loads(response.text)
    eskiz = SMSProvider.objects.first()
    eskiz.token = data['data']['token']
    eskiz.save()
    return data['data']['token']

def send_message(phone, device_id):
    otp = generateOTP(phone)
    send_url = BASE_URL + "/message/sms/send"
    token = SMSProvider.objects.first().token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    # Vash kod podtverjdeniya dlya mobilnogo prilojeniya Avtoritet Group:
    data = {
        'mobile_phone':phone[1:],
        'message':f"<#> Your verification code Orient Motors: {otp} {device_id}", 
        'from':'4546'
    }
    
    resp =requests.post(url=send_url, data=data, headers=headers)

    if resp.status_code == 401:
        token = refresh_token()
        
        headers = {
            'Authorization': f'Bearer {token}'
        }
        resp =requests.post(url=send_url, data=data, headers=headers)
        


    return resp


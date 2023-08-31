from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema, ManualSchema



login_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='phone',
        required=True,
        description="User phone number",
        type='char',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='password',
        required=True,
        description="password",
        type='char',
        location='form',
        schema=coreschema.String()
    ),
])

send_otp_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='phone',
        required=True,
        description="User phone number",
        type='char',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='device_id',
        required=True,
        description="mobile device id",
        type='char',
        location='form',
        schema=coreschema.String()
    ),
])

verify_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='phone',
        required=True,
        description="User phone number",
        type='char',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='code',
        required=True,
        description="otp code witch sent via sms",
        type='char',
        location='form',
        schema=coreschema.String()
    ),
])
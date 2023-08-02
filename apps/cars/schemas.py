from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema

body_type_with_count_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='model_id',
        required=False,
        description="Car model's id",
        type='integer',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='min_year',
        required=False,
        description="Min manufactured year",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='max_year',
        required=False,
        description="Max manufactured year",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='min_month',
        required=False,
        description="Min manufactured month",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='max_month',
        required=False,
        description="Max manufactured month",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='min_mileage',
        required=False,
        description="Min mileage",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='max_mileage',
        required=False,
        description="Max mileage",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='min_price',
        required=False,
        description="Min price",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='max_price',
        required=False,
        description="Max price",
        type='intager',
        location='path',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='currency',
        required=False,
        description="Currency of price",
        type='string',
        location='path',
        schema=coreschema.String()
    ),

])


service_info_list_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='service_id',
        required=True,
        description="Service id",
        type='integer',
        location='path',
        schema=coreschema.String()
    ),
])
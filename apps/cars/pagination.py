from rest_framework.pagination import PageNumberPagination


class CarsListPagination(PageNumberPagination):
    page_size = 10
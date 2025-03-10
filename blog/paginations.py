from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'results': data
        })

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = 20 if not request.query_params.get('size') else int(request.query_params.get('size'))
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'pages': {
                'next': self.page.next_page_number() if self.page.has_next() else '',
                'previous': self.page.previous_page_number() if self.page.has_previous() else '',
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'page_size': self.page_size
            },
            'count': self.page.paginator.count,
            'results': data
        })
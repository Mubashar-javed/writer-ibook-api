from rest_framework import pagination


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = "page_size"  # query param to override default page size
    max_page_size = 100  # stop users from requesting too many results

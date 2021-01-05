from rest_framework.pagination import PageNumberPagination


class My_Pagination(PageNumberPagination):
    page_size = 3  # number of list items to be in one page

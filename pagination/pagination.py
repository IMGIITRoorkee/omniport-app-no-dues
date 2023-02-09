from rest_framework.pagination import PageNumberPagination

class StandardPagination(PageNumberPagination):
    """
    Pagnination class used for showing 
    various permission status' in no_dues
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
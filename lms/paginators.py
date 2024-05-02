from rest_framework.pagination import PageNumberPagination


class LessonPagination(PageNumberPagination):
    # Количество элементов на странице
    page_size = 1
    # Параметр запроса количества элементов на странице
    page_size_query_param = ('page_size')
    # Максимальное количество элементов на странице
    max_page_size = 20


class CoursePagination(PageNumberPagination):
    # Количество элементов на странице
    page_size = 1
    # Параметр запроса количества элементов на странице
    page_size_query_param = ('page_size')
    # Максимальное количество элементов на странице
    max_page_size = 20

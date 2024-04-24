from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer
from users.models import Payments


class CourseViewSet(viewsets.ModelViewSet):
    '''Описываем ViewSet для работы с моделью (просмотр списка курсов).'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return CourseSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    '''Контроллеры на основе дженерик (создание урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка уроков).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course',)
    ordering_fields = ('payment_date', 'course', 'payment_method',)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''Контроллеры на основе дженерик (просмотр одного урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''Контроллеры на основе дженерик (редактирование урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''Контроллеры на основе дженерик (удаление урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка платежей)'''
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method',)
    ordering_fields = ('payment_date',)
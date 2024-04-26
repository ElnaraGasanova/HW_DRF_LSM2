from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    '''Описываем ViewSet для работы с моделью (просмотр списка курсов).'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]


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

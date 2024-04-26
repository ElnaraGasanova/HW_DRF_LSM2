from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    '''Описываем ViewSet для работы с моделью (просмотр списка курсов).'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [IsOwner, ~IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner, ~IsModerator]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    '''Контроллеры на основе дженерик (создание урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [~IsModerator]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonListAPIView(generics.ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка уроков).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course',)
    ordering_fields = ('payment_date', 'course', 'payment_method',)
    permission_classes = [IsOwner, ~IsModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''Контроллеры на основе дженерик (просмотр одного урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, ~IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''Контроллеры на основе дженерик (редактирование урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, ~IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''Контроллеры на основе дженерик (удаление урока).'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, ~IsModerator]

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserCreateAPIView(CreateAPIView):
    '''Контроллеры на основе дженерик (создание пользователя).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка пользователей).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(UpdateAPIView):
    '''Контроллеры на основе дженерик (редактирование пользователя).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserDestroyAPIView(DestroyAPIView):
    '''Контроллеры на основе дженерик (удаление пользователя).'''
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class PaymentsCreateAPIView(CreateAPIView):
    '''Контроллеры на основе дженерик (создание платежа).'''
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        # user = serializer.save(is_active=True)
        # user.set_password(user.password)
        # user.save()
        pass


class PaymentsListAPIView(generics.ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка платежей)'''
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method',)
    ordering_fields = ('payment_date',)
    permission_classes = (IsAuthenticated,)

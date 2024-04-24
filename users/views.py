from rest_framework import viewsets, generics
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''Описываем ViewSet для работы с моделью (просмотр списка пользователей).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка пользователей).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(generics.RetrieveAPIView):
    '''Контроллеры на основе дженерик (просмотр пользователя)'''
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    '''Контроллеры на основе дженерик (редактирование пользователя)'''
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyView(generics.DestroyAPIView):
    '''Контроллеры на основе дженерик (удаление пользователя)'''
    serializer_class = UserSerializer
    queryset = User.objects.all()

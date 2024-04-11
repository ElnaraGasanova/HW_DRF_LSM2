from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', help_text='Укажите почту')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', help_text='Укажите номер телефона',
                             **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', help_text='Укажите город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatar', verbose_name='Аватар', help_text='Загрузите фото',
                               **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

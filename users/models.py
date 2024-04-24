from django.contrib.auth.models import AbstractUser
from django.db import models
from lms.models import Course, Lesson

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


class Payments(models.Model):

    PAYMENT_METHOD = [('cash', 'Наличные'), ('transfer', 'Перевод на счет')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='payments')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    course_paid = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс',
                                    related_name='payments', **NULLABLE)
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок',
                                    related_name='payments', **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=100, verbose_name='Способ оплаты')

    def __str__(self):
        return f'Оплата от {self.user} в размере {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('user', 'payment_date',)

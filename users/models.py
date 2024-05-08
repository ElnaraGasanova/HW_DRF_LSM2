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
                             related_name='payments', **NULLABLE)
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты', **NULLABLE)
    course_paid = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс',
                                    related_name='payments', **NULLABLE)
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок',
                                    related_name='payments', **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты',
                                 help_text='Укажите сумму платежа')
    payment_method = models.CharField(max_length=100, verbose_name='Способ оплаты', **NULLABLE)
    payment_link = models.URLField(max_length=400, verbose_name='Ссылка на оплату',
                                   help_text='Укажите ссылку на оплату', **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='ID Сессии', help_text='Укажите ID Сессии',
                                  **NULLABLE)


    def __str__(self):
        return f'Оплата от {self.user} в размере {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('user', 'payment_date',)

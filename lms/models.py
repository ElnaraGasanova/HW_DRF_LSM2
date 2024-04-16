from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Укажите наименование курса')
    image = models.ImageField(upload_to='courses_image', verbose_name='Превью', help_text='Загрузите превью курса',
                              **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        '''Добавляем строковое отображение это будет выводиться на сайте в карточке!'''
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Укажите наименование урока')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='lessons_image', verbose_name='Превью', help_text='Загрузите превью урока',
                              **NULLABLE)
    video_link = models.URLField(verbose_name='Ссылка', help_text='Укажите ссылку на видео', **NULLABLE)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE,
                               verbose_name='Курс', help_text='Укажите наименование курса', **NULLABLE)

    def __str__(self):
        '''Добавляем строковое отображение это будет выводиться на сайте в карточке!'''
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


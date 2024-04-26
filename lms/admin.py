from django.contrib import admin
from lms.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''Отображение списка Курсов'''
    list_display = ('name', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    '''Отображение списка Уроков'''
    list_display = ('name', 'course', 'owner',)
    search_fields = ('name',)

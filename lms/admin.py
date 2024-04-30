from django.contrib import admin
from lms.models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''Отображение списка Курсов'''
    list_display = ('name', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    '''Отображение списка Уроков'''
    list_display = ('name', 'course', 'owner',)
    search_fields = ('name',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    '''Отображение списка Уроков'''
    list_display = ('user', 'course', 'subscription_is_active',)
    search_fields = ('user',)

from rest_framework import serializers
from lms.models import Course, Lesson
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    '''Добавляем поле вывода количества уроков.'''
    lessons_count = serializers.SerializerMethodField(default=0)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        #пеереопределяем метод
        return instance.lesson_set.count()

    # def get_lessons_count(self, instance):
    #     if instance.lessons:
    #         return instance.lessons.count()
    #     else:
    #         return 0


class PaymentsSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = Payments
        fields = '__all__'

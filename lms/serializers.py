from rest_framework import serializers
from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    '''Добавляем поле вывода количества уроков.'''
    lessons_count = serializers.SerializerMethodField(default=0)

    def get_lessons_count(self, instance):
        #пеереопределяем метод
        return instance.lesson.count()

    # def get_lessons_count(self, instance):
    #     if instance.lessons:
    #         return instance.lessons.count()
    #     else:
    #         return 0

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = Lesson
        fields = '__all__'

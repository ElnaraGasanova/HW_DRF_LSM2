from rest_framework import serializers
from lms.models import Course, Lesson, Subscription
from lms.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор урока.'''
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    '''Добавляем поле вывода количества уроков.'''
    lessons_count = serializers.SerializerMethodField(default=0)
    lesson = LessonSerializer(source='courses', many=True, read_only=True)
    subscription_is_active = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        validators = [URLValidator(field='video_link')]

    def get_lessons_count(self, instance):
        '''Переопределяем метод.'''
        return instance.courses.count()

    def get_subscription_is_active(self, instance):
        '''Наличие подписки у пользователя.'''
        user = self.context["request"].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, courses=instance, subscription_is_active=True).exists()
        return False


class SubscriptionSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор подписки.'''
    class Meta:
        model = Subscription
        fields = '__all__'

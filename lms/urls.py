from django.urls import path
from rest_framework.routers import DefaultRouter
from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView,
                       LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
# подключаем набор контроллеров на основе ViewSet
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
] + router.urls

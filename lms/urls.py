from django.urls import path
from rest_framework.routers import DefaultRouter
from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView,
                       LessonUpdateAPIView, LessonDestroyAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
#подключаем набор контроллеров на основе ViewSet
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_get'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
] + router.urls

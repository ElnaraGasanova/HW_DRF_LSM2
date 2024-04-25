from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
#подключаем набор контроллеров на основе ViewSet
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
] + router.urls
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
#подключаем набор контроллеров на основе ViewSet
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
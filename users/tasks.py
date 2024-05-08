from datetime import datetime, timedelta
from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def user_blocking():
    '''Функция блокирования пользователя, если он не заходил более месяца.'''
    user_is_active = User.objects.filter(is_active=True)
    today = datetime.now().date()
    for user in user_is_active:
        if user.last_login and (today - user.last_login.date()) > timedelta(days=30):
            user.is_active = False
            user.save()

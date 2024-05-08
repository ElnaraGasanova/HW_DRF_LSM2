from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from lms.models import Subscription


@shared_task
def send_message_for_update(course_id):
    '''Отправка уведомления об обновлениях по подписке.'''
    subs_update = Subscription.objects.filter(course=course_id)
    subject = 'Обновление'
    message = 'Вы подписаны на обновления курса, вышла новая информция.'
    if subs_update:
        email_list = []
        for subscr in subs_update:
            email_list.append(subscr.user.email)
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_list,
            fail_silently=True
        )
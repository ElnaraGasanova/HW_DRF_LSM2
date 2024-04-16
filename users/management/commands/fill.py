from datetime import datetime
from django.core.management import BaseCommand
from lms.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        '''Создаем список, которым хотим заполнить БД'''
        # Удаляем все платежи, если были
        Payments.objects.all().delete()

        user1, created = User.objects.get_or_create(email='user1@test.ru')
        user2, created = User.objects.get_or_create(email='user2@test.ru')
        user3, created = User.objects.get_or_create(email='user3@test.ru')
        user4, created = User.objects.get_or_create(email='user4@test.ru')

        course1, created = Course.objects.get_or_create(name='Django')
        course2, created = Course.objects.get_or_create(name='React')
        course3, created = Course.objects.get_or_create(name='JS')
        course4, created = Course.objects.get_or_create(name='Python')

        lesson1, created = Lesson.objects.get_or_create(name='Module1')
        lesson2, created = Lesson.objects.get_or_create(name='Module2')
        lesson3, created = Lesson.objects.get_or_create(name='FULL Module')
        lesson4, created = Lesson.objects.get_or_create(name='IND Module')


        # БД платежей
        Payments.objects.create(
            user=user1,
            payment_date=datetime.now().date,
            course_paid=course1,
            lesson_paid=lesson1,
            amount=78000,
            payment_method='transfer'
        )
        Payments.objects.create(
            user=user2,
            payment_date=datetime.now().date,
            course_paid=course2,
            lesson_paid=lesson2,
            amount=99000,
            payment_method='cash'
        )
        Payments.objects.create(
            user=user3,
            payment_date=datetime.now().date,
            course_paid=course3,
            lesson_paid=lesson3,
            amount=178000,
            payment_method='transfer'
        )
        Payments.objects.create(
            user=user4,
            payment_date=datetime.now().date,
            course_paid=course4,
            lesson_paid=lesson4,
            amount=238000,
            payment_method='transfer'
        )

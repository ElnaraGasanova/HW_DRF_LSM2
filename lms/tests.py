from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test_admin@sky.pro')
        self.course = Course.objects.create(name='C++', description='Язык программирования общего назначения')
        self.lesson = Lesson.objects.create(name='Test_Modul', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('lms:lesson_get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse('lms:lesson_create')
        data = {
            "name": "Testing_Lesson",
            "description": "Тестируемся",
            "video_link": "https://www.youtube.com/watch?v=EVrMbS14FdE",
            "course": 1
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('lms:lesson_update', args=(self.lesson.pk,))
        data = {
            "name": "Test2_Lesson2",
            "description": "Редактиреум"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Test2_Lesson2"
        )

    def test_lesson_delete(self):
        url = reverse('lms:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('lms:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result ={
            "count": 1,
            "next": None,
            "previous": None,
            "results":[
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "image": None,
                    "video_link": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                },
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


# class CourseTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(email='test_admin@sky.pro')
#         self.course = Course.objects.create(name='C++', description='Язык программирования общего назначения',
#                                             owner=self.user)
#         self.lesson = Lesson.objects.create(name='Test_Modul', course=self.course, owner=self.user)
#         self.client.force_authenticate(user=self.user)
#
#     def test_course_retrieve(self):
#         url = reverse('lms:courses-detail', args=(self.course.pk,))
#         response = self.client.get(url)
#         data = response.json()
#         self.assertEqual(
#             response.status_code, status.HTTP_200_OK
#         )
#         self.assertEqual(
#             data.get('name'), self.course.name
#         )

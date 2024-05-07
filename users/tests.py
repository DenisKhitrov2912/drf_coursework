from rest_framework.test import APITestCase, APIClient
from users.models import User
from django.urls import reverse
from rest_framework import status


class UserTestCase(APITestCase):
    """Тест пользователей"""

    def setUp(self) -> None:
        """Создание условий для теста"""
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='12345')
        self.client.force_authenticate(user=self.user)

    def test_list_users(self):
        """Тест списка пользователей"""
        response = self.client.get(
            reverse('users:users'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': self.user.pk, 'email': 'test@test.com', 'avatar': None, 'phone': None, 'city': None}]
        )

    def test_create_user(self):
        """Тест создания пользователей"""
        data = {
            "email": '1@ya.ru',
            "password": "123456"
        }
        response = self.client.post(reverse('users:user_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                         {'id': self.user.pk + 1, 'email': '1@ya.ru', 'avatar': None, 'phone': None, 'city': None,
                          'password': '123456'})

    def test_retrieve_user(self):
        """Тест просмотра пользователя"""
        response = self.client.get(
            reverse('users:user', kwargs={'pk': self.user.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {'id': self.user.pk, 'email': 'test@test.com', 'avatar': None, 'phone': None, 'city': None,
                          'password': '12345'})

    def test_update_user(self):
        """Тест обновления пользователя"""
        data = {
            "email": '12@ya.ru',
            "password": "1234567"
        }
        response = self.client.patch(
            reverse('users:user_update', kwargs={'pk': self.user.pk}),

            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.user.pk, 'email': '12@ya.ru', 'avatar': None, 'phone': None, 'city': None,
             'password': '1234567'}
        )

    def test_delete_user(self):
        """Тест удаления пользователя"""
        response = self.client.delete(
            reverse('users:user_delete', kwargs={'pk': self.user.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

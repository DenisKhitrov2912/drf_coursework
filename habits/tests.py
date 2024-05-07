from rest_framework.test import APITestCase, APIClient
from users.models import User
from habits.models import Habit
from django.urls import reverse
from rest_framework import status


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='12345')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(user=self.user, place='1', time='18:00:00', action='2', periodicity=2,
                                          time_to_complete=100, is_public=True)

    def test_list_habits(self):
        response = self.client.get(
            reverse('habits:habits'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': self.habit.id,
                          'action': '2',
                          'is_nice_habit': None,
                          'is_public': True,
                          'periodicity': 2,
                          'place': '1',
                          'related_habit': None,
                          'reward': None,
                          'time': '18:00:00',
                          'time_to_complete': 100,
                          'user': self.user.id}]}
        )

    def test_create_habit(self):
        data = {
            'action': '3',
            'is_public': True,
            'periodicity': 3,
            'place': '3',
            'time': '18:30:00',
            'time_to_complete': 100,
            'user': '1'}
        response = self.client.post(reverse('habits:habit_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                         {'id': self.habit.id + 1,
                          'action': '3',
                          'is_nice_habit': None,
                          'is_public': True,
                          'periodicity': 3,
                          'place': '3',
                          'related_habit': None,
                          'reward': None,
                          'time': '18:30:00',
                          'time_to_complete': 100,
                          'user': self.user.id})

    def test_retrieve_habit(self):
        response = self.client.get(
            reverse('habits:habit', kwargs={'pk': self.habit.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {'id': self.habit.id,
                          'action': '2',
                          'is_nice_habit': None,
                          'is_public': True,
                          'periodicity': 2,
                          'place': '1',
                          'related_habit': None,
                          'reward': None,
                          'time': '18:00:00',
                          'time_to_complete': 100,
                          'user': self.user.id})

    def test_update_habit(self):
        data = {
            'action': '3',
            'periodicity': 5
        }
        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),

            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.habit.id,
             'action': '3',
             'is_nice_habit': None,
             'is_public': True,
             'periodicity': 5,
             'place': '1',
             'related_habit': None,
             'reward': None,
             'time': '18:00:00',
             'time_to_complete': 100,
             'user': self.user.id}
        )

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': self.habit.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_validator_rel_rew(self):
        data = {
            'id': self.habit.id,
            'action': '3',
            'is_public': True,
            'periodicity': 5,
            'place': '1',
            'related_habit': self.habit.id,
            'reward': '1000',
            'time': '18:00:00',
            'time_to_complete': 100,
            'user': self.user.id
        }
        response = self.client.post(reverse('habits:habit_create'), data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        print(response.json())

        self.assertEqual(
            response.json(),
            {'video': ['Incorrect YouTube URL']}
        )

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habits.models import Habit
from habits.paginators import HabitsPagination
from habits.serializers import HabitSerializer
from users.permissions import IsUserOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """Список привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsUserOwner | IsAdminUser]

    def get(self, request):
        if not self.request.user.is_superuser:
            queryset = Habit.objects.filter(user=self.request.user)
        else:
            queryset = Habit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Одна привычка"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner | IsAdminUser]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner | IsAdminUser]


class HabitPublicListAPIView(generics.ListAPIView):
    """Список публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]

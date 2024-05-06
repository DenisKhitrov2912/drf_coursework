from django.shortcuts import render
from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    #permission_classes = [IsAuthenticated, IsAdminUser | IsUserOwner]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated]
    #pagination_class = MaterialsPagination



    # def get(self, request):
    #     queryset = Lesson.objects.all()
    #     paginated_queryset = self.paginate_queryset(queryset)
    #     serializer = LessonSerializer(paginated_queryset, many=True)
    #     return self.get_paginated_response(serializer.data)


class HabitDetailAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated, IsUserAdmDRF | IsUserOwner]
    # pagination_class = MaterialsPagination


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsUserAdmDRF | IsUserOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsAdminUser | IsUserOwner]
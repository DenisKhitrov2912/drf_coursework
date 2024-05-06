from django.urls import path


from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitDetailAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/', HabitListAPIView.as_view(), name='habits'),
    path('habit/<int:pk>/', HabitDetailAPIView.as_view(), name='habit'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]

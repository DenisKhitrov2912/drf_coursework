from django.apps import apps
from rest_framework.exceptions import ValidationError


def validate_related_habit_and_reward(habit):
    """Валидатор на вознаграждение и связанную привычку"""
    if habit.related_habit and habit.reward:
        raise ValidationError('Нельзя одновременно выбирать связанную'
                              ' привычку и указывать вознаграждение.')


def validate_time_to_complete(habit):
    """Валидатор на время выполнения"""
    if habit.time_to_complete > 120:
        raise ValidationError('Время выполнения должно быть'
                              ' не больше 120 секунд.')


def validate_nice_habit_no_reward_or_related(habit):
    """Валидатор на отсутствие награды или
     связанной привычки у приятной привычки"""
    if habit.is_nice_habit and (habit.reward or habit.related_habit):
        raise ValidationError('У приятной привычки не может'
                              ' быть вознаграждения или связанной привычки.')


def validate_periodicity(habit):
    """Валидатор на периодичность в днях"""
    if habit.periodicity > 7:
        raise ValidationError('Нельзя выполнять привычку реже,'
                              ' чем 1 раз в 7 дней.')


def validate_related_habit_is_nice(habit):
    """Валидатор на связанные и приятные привычки"""
    if habit.related_habit:
        habit_mod = apps.get_model('habits', 'Habit')
        related_habits = habit_mod.objects.filter(pk=habit.related_habit.id)
        if not all(h.is_nice_habit for h in related_habits):
            raise ValidationError('В связанные привычки могут '
                                  'попадать только привычки с признаком '
                                  'приятной привычки.')

from django.db import models

from habits.validators import validate_related_habit_and_reward, validate_time_to_complete, \
    validate_nice_habit_no_reward_or_related, validate_periodicity, validate_related_habit_is_nice

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место выполнения')
    time = models.TimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_nice_habit = models.BooleanField(verbose_name='приятность привычки', **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка',
                                      **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(verbose_name='интервал между привычками в днях')
    reward = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveSmallIntegerField(verbose_name='время на выполнение в секундах')
    is_public = models.BooleanField(verbose_name='публичность')

    def __str__(self):
        return f"{self.user}, {self.action}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def clean(self):
        validate_related_habit_and_reward(self)
        validate_time_to_complete(self)
        validate_nice_habit_no_reward_or_related(self)
        validate_periodicity(self)
        validate_related_habit_is_nice(self)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Habit, self).save(*args, **kwargs)

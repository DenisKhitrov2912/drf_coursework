import os
from celery import shared_task
from datetime import timedelta

from django.utils import timezone

from habits.models import Habit
from habits.services import send_message


@shared_task
def tlg_sending():
    """Функция рассылки в телеграме"""
    time_now = timezone.now()
    habits = Habit.objects.all()
    token = os.getenv('TELEGRAM_TOKEN')
    time_start = time_now - timedelta(minutes=5)
    time_end = time_now + timedelta(minutes=5)

    for habit in habits:
        if time_start.time() <= habit.time <= time_end.time():
            if habit.last_reminder is None or (time_now - habit.last_reminder).days >= habit.periodicity:
                message = f"""Напоминание о привычке: {habit.action}.
Займитесь приятной привычкой или получите вознаграждение после выполнения!"""
                send_message(token=token,
                             chat_id=habit.user.chat_id,
                             message=message)
                habit.last_reminder = time_now
                habit.save()

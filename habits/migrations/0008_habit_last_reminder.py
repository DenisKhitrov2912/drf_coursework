# Generated by Django 5.0.4 on 2024-05-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_alter_habit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='last_reminder',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата последнего напоминания'),
        ),
    ]

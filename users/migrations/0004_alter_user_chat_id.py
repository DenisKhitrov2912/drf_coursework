# Generated by Django 5.0.4 on 2024-05-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.CharField(max_length=100, verbose_name='аккаунт в телеграм'),
        ),
    ]

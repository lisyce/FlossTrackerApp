# Generated by Django 4.1.2 on 2022-10-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_userthread_unique_user_thread'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userthread',
            constraint=models.UniqueConstraint(fields=('thread_data', 'owner'), name='unique_user_thread'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-27 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_brand_name_threadcolor_unique_brand_color_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userthread',
            name='unique_user_thread',
        ),
    ]

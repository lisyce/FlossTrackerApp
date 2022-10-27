# Generated by Django 4.1.2 on 2022-10-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_userthread_unique_user_thread'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='threadcolor',
            name='unique_brand_color',
        ),
        migrations.AddConstraint(
            model_name='threadcolor',
            constraint=models.UniqueConstraint(fields=('brand', 'brand_number'), name='unique_brand_number'),
        ),
        migrations.AddConstraint(
            model_name='threadcolor',
            constraint=models.UniqueConstraint(fields=('brand', 'name'), name='unique_brand_color_name'),
        ),
    ]

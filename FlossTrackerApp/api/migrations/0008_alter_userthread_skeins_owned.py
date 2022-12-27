# Generated by Django 4.1.2 on 2022-12-27 04:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_threadcolor_unique_brand_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userthread',
            name='skeins_owned',
            field=models.DecimalField(decimal_places=2, default=-1.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
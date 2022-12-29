# Generated by Django 3.2.10 on 2022-01-26 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0023_auto_20220124_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericsettings',
            name='custom_carrier_name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9_]+$')]),
        ),
    ]

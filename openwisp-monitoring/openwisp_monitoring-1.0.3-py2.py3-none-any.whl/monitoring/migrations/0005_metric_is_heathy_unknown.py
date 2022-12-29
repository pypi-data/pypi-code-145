# Generated by Django 3.0.4 on 2020-04-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('monitoring', '0004_move_notifications')]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='is_healthy',
            field=models.BooleanField(
                db_index=True, default=None, null=True, blank=True
            ),
        )
    ]

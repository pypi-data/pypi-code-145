# Generated by Django 3.2.14 on 2022-09-06 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0037_chronopostsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericsettings',
            name='label_template',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.labeltemplate'),
        ),
    ]

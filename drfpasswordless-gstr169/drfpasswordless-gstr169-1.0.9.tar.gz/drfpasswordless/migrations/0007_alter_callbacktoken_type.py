# Generated by Django 3.2.16 on 2022-12-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfpasswordless', '0006_auto_20221228_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbacktoken',
            name='type',
            field=models.CharField(choices=[('AUTH', 'Auth'), ('VERIFY', 'Verify'), ('CHANGE', 'Change')], max_length=20),
        ),
    ]

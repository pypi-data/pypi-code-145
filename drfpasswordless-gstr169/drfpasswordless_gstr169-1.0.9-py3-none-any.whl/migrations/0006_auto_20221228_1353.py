# Generated by Django 3.1.14 on 2022-12-28 13:53

from django.db import migrations, models
import drfpasswordless.models


class Migration(migrations.Migration):

    dependencies = [
        ('drfpasswordless', '0005_auto_20201117_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbacktoken',
            name='key',
            field=models.TextField(default=drfpasswordless.models.generate_numeric_token),
        ),
    ]

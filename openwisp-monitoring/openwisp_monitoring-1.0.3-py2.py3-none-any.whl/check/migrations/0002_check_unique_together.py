# Generated by Django 2.0.2 on 2018-03-05 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='check', unique_together={('name', 'object_id', 'content_type')}
        )
    ]

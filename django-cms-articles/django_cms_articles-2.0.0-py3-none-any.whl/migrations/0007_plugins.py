# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 12:45
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_plugins(apps, schema_editor):
    ArticlesPlugin = apps.get_model("cms_articles", "ArticlesPlugin")

    for p in ArticlesPlugin.objects.all():
        if p.tree:
            p.trees.add(p.tree)


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0001_initial"),
        ("cms_articles", "0006_order_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlesplugin",
            name="trees",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="_articlesplugin_trees_+", to="cms.Page", verbose_name="trees"
            ),
        ),
        migrations.RunPython(migrate_plugins),
        migrations.RemoveField(
            model_name="articlesplugin",
            name="tree",
        ),
    ]

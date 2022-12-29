# Generated by Django 3.0.7 on 2020-06-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akas',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('aka', models.CharField(blank=True, max_length=30, null=True)),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'akas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('ra_original', models.FloatField()),
                ('decl_original', models.FloatField()),
                ('date_inserted', models.DateTimeField()),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('year', models.PositiveSmallIntegerField()),
                ('base26suffix', models.CharField(max_length=20)),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2016',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2016',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2017',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2017',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2018',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2018',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2019',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2019',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2020',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2020',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2021',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2021',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2022',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2022',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2023',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2023',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2024',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2024',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2025',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2025',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2026',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2026',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2027',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2027',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2028',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2028',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2029',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2029',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Y2030',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('ra', models.FloatField()),
                ('decl', models.FloatField()),
                ('survey_database', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_inserted', models.DateTimeField()),
                ('htm16id', models.BigIntegerField(db_column='htm16ID')),
            ],
            options={
                'db_table': 'y2030',
                'managed': False,
            },
        ),
    ]

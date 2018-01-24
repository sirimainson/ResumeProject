# Generated by Django 2.0.1 on 2018-01-23 17:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_no', models.CharField(max_length=10)),
                ('village_no', models.CharField(max_length=3)),
                ('alley', models.CharField(max_length=20)),
                ('road', models.CharField(max_length=20)),
                ('sub_area', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.CharField(choices=[('b', 'Beginner'), ('e', 'Elementary'), ('i', 'Intermediate'), ('a', 'Advanced'), ('p', 'Proficiency')], default='b', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=32)),
                ('person_name', models.CharField(max_length=32)),
                ('contents', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=[], size=10)),
                ('date', models.CharField(default='-/-/-', max_length=32)),
                ('time_period', models.CharField(default='xx/xx - yy/yy', max_length=20)),
                ('attachments', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), default=[], size=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]
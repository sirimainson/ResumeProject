# Generated by Django 2.0.1 on 2018-01-25 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0003_skill_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reference',
            old_name='Affiliation',
            new_name='affiliation',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='postion',
            new_name='position',
        ),
    ]

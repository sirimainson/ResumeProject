# Generated by Django 2.0.1 on 2018-02-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0003_auto_20180208_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
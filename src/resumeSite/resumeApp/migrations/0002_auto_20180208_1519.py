# Generated by Django 2.0.1 on 2018-02-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

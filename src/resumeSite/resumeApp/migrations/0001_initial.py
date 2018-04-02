# Generated by Django 2.0.1 on 2018-02-06 12:35

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academy_name', models.CharField(max_length=64)),
                ('level', models.CharField(choices=[('el', 'Elementary'), ('se', 'Secondary'), ('un', 'Undergraduate'), ('ms', 'Master'), ('dr', 'Doctorate')], default='un', max_length=2)),
                ('time_period', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('role', models.TextField(blank=True, max_length=400)),
                ('time_period', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('level', models.CharField(choices=[('b', 'Beginner'), ('e', 'Elementary'), ('i', 'Intermediate'), ('a', 'Advanced'), ('p', 'Proficiency')], default='b', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=128)),
                ('position', models.CharField(choices=[('dr', 'ผู้อำนวยการ'), ('hr', 'ผู้จัดการฝ่ายทรัพยากรบุคคล'), ('ot', 'อื่นๆ โปรดระบุ')], default='hr', max_length=64)),
                ('position_other', models.CharField(blank=True, max_length=64)),
                ('contents', models.TextField(max_length=5000)),
                ('date', models.DateField()),
                ('time_period', models.CharField(default='xx/xx - yy/yy', max_length=32)),
                ('language', models.CharField(choices=[('th', 'Thai'), ('en', 'English')], default='TH', max_length=2)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('attachment', models.ManyToManyField(blank=True, related_name='student_attachment', to='resumeApp.Attachment')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=64)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeApp.Branch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resumeApp.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor_name', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('affiliation', models.CharField(max_length=64)),
                ('phone_no', models.CharField(max_length=10)),
                ('email', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), default=[], size=2)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('level', models.CharField(choices=[('b', 'Beginner'), ('e', 'Elementary'), ('i', 'Intermediate'), ('a', 'Advanced'), ('p', 'Proficiency')], default='b', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name_th', models.CharField(max_length=32)),
                ('last_name_th', models.CharField(max_length=32)),
                ('first_name_en', models.CharField(max_length=32)),
                ('last_name_en', models.CharField(max_length=32)),
                ('address_th', models.TextField(max_length=640)),
                ('address_en', models.TextField(max_length=640)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('phone_no', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=2)),
                ('email', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), size=2)),
                ('birthday', models.DateField()),
                ('nationality', models.CharField(max_length=16)),
                ('religion', models.CharField(blank=True, choices=[('b', 'Buddistsm'), ('c', 'Christians'), ('h', 'Hinduism')], max_length=16, null=True)),
                ('age', models.IntegerField(default=0)),
                ('activity', models.TextField(max_length=500)),
                ('hobby', models.TextField(max_length=500)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('education', models.ManyToManyField(related_name='student_education', to='resumeApp.Education')),
                ('experience', models.ManyToManyField(related_name='student_experience', to='resumeApp.Experience')),
                ('language', models.ManyToManyField(related_name='student_language', to='resumeApp.Language')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeApp.Reference')),
                ('skill', models.ManyToManyField(related_name='student_skill', to='resumeApp.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='letter',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeApp.Major'),
        ),
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeApp.Major'),
        ),
    ]
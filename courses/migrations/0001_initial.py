# Generated by Django 5.0.6 on 2024-07-09 12:57

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('course_id', models.CharField(blank=True, max_length=20, null=True)),
                ('duration_h', models.TimeField()),
                ('duration_m', models.IntegerField(help_text='Bu yerda kurs davomiyligi necha oy bolishi kiritiladi')),
                ('price', models.IntegerField(help_text='Kurs narxi uzs da')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('days', multiselectfield.db.fields.MultiSelectField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=20)),
                ('lesson_start_time', models.TimeField()),
                ('group_opened_time', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.room')),
            ],
        ),
    ]

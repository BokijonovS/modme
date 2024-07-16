# Generated by Django 5.0.6 on 2024-07-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_dailystat_delete_dailystudentstat'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduatedStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('student_name', models.CharField(max_length=100)),
            ],
        ),
    ]

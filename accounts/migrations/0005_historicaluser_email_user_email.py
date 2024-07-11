# Generated by Django 5.0.6 on 2024-07-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]

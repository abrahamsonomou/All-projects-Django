# Generated by Django 4.1 on 2022-08-05 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 9, 41, 37, 663018, tzinfo=datetime.timezone.utc)),
        ),
    ]

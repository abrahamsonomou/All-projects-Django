# Generated by Django 4.1 on 2022-08-07 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriel', '0005_alter_tutoriel_plublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 0, 43, 5, 786645, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 4.1 on 2022-08-07 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriel', '0006_alter_tutoriel_plublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 0, 49, 1, 223243, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 4.1 on 2022-08-05 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriel', '0004_alter_tutoriel_plublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 17, 17, 25, 834164, tzinfo=datetime.timezone.utc)),
        ),
    ]
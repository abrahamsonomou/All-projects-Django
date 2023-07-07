# Generated by Django 4.0.4 on 2022-05-26 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_formation', '0007_alter_cours_plublish_alter_lecon_plublish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 9, 25, 47, 710213, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lecon',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 9, 25, 47, 710213, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 9, 25, 47, 710213, tzinfo=utc)),
        ),
    ]

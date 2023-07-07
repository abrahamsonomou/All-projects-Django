# Generated by Django 4.0.4 on 2022-05-30 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_formation', '0015_rename_category_formation_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 11, 36, 4, 788013, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lecon',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 11, 36, 4, 789010, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 11, 36, 4, 789010, tzinfo=utc)),
        ),
    ]
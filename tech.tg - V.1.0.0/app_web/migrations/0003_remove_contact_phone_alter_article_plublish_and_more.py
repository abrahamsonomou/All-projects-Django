# Generated by Django 4.0.4 on 2022-05-23 06:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0002_remove_temoignage_titre_temoignage_fullname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AlterField(
            model_name='article',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 6, 59, 56, 429509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 6, 59, 56, 429509, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-30 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0015_alter_article_plublish_alter_commentaire_plublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 11, 36, 4, 794995, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 11, 36, 4, 794995, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_formation', '0012_rename_category_tutoriel_categorie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutoriel',
            old_name='user',
            new_name='auteur',
        ),
        migrations.AlterField(
            model_name='cours',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 11, 22, 37, 750133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lecon',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 11, 22, 37, 750133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 11, 22, 37, 750133, tzinfo=utc)),
        ),
    ]

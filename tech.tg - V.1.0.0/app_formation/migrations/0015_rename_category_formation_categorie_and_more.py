# Generated by Django 4.0.4 on 2022-05-26 20:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_formation', '0014_formation_remove_lecon_cours_alter_lecon_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formation',
            old_name='category',
            new_name='categorie',
        ),
        migrations.AlterField(
            model_name='formation',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 20, 1, 55, 2042, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lecon',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 20, 1, 55, 2042, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 20, 1, 55, 2042, tzinfo=utc)),
        ),
    ]

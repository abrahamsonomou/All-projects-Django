# Generated by Django 4.0.6 on 2022-07-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='grade',
            field=models.TextField(blank=True, choices=[('bts', 'BTS'), ('licence', 'Licence'), ('autre', 'Autre'), ('master', 'Master'), ('doctorat', 'Doctorat')], null=True, verbose_name='Grade'),
        ),
    ]
# Generated by Django 4.1.1 on 2022-11-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.TextField(blank=True, choices=[('bts', 'BTS'), ('doctorat', 'Doctorat'), ('autre', 'Autre'), ('licence', 'Licence'), ('master', 'Master')], null=True, verbose_name='Grade'),
        ),
    ]

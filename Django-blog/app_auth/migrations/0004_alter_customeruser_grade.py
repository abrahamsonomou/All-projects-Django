# Generated by Django 4.0.6 on 2022-07-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_alter_customeruser_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='grade',
            field=models.TextField(blank=True, choices=[('autre', 'Autre'), ('doctorat', 'Doctorat'), ('bts', 'BTS'), ('licence', 'Licence'), ('master', 'Master')], null=True, verbose_name='Grade'),
        ),
    ]

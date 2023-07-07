# Generated by Django 4.1 on 2022-08-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_alter_customuser_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.TextField(blank=True, choices=[('master', 'Master'), ('licence', 'Licence'), ('doctorat', 'Doctorat'), ('bts', 'BTS'), ('autre', 'Autre')], null=True, verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='session_token',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
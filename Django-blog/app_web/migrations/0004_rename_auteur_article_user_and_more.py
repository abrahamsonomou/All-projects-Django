# Generated by Django 4.0.6 on 2022-07-16 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0003_alter_article_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auteur',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='commentaire',
            old_name='auteur',
            new_name='user',
        ),
    ]

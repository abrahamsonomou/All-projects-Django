# Generated by Django 4.0.6 on 2022-07-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0002_remove_article_tags_alter_article_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.CharField(choices=[('corbeille', 'corbeille'), ('publie', 'publié')], default='corbeille', max_length=200, verbose_name='Statut'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 19:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_formation', '0013_rename_user_tutoriel_auteur_alter_cours_plublish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Slug')),
                ('description1', models.TextField(blank=True, null=True, verbose_name='Description1')),
                ('description2', django_quill.fields.QuillField(blank=True, null=True, verbose_name='Description2')),
                ('image', models.ImageField(blank=True, null=True, upload_to='formations', verbose_name='Image')),
                ('plublish', models.DateTimeField(default=datetime.datetime(2022, 5, 26, 19, 25, 51, 73054, tzinfo=utc))),
                ('published', models.BooleanField(default=False, verbose_name='Publie')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_user', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_category', to='app_formation.category', verbose_name='Category')),
                ('niveau', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_formation.niveau', verbose_name='niveau')),
            ],
            options={
                'verbose_name': 'Formation',
            },
        ),
        migrations.RemoveField(
            model_name='lecon',
            name='cours',
        ),
        migrations.AlterField(
            model_name='lecon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='formations', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='lecon',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 19, 25, 51, 74076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutoriel',
            name='plublish',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 19, 25, 51, 75073, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
        migrations.AddField(
            model_name='lecon',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_formations', to='app_formation.formation', verbose_name='Formations'),
        ),
    ]

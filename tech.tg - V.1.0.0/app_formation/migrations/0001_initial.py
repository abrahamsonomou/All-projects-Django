# Generated by Django 4.0.4 on 2022-05-21 11:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_quill.fields
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Libelle')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Slug')),
                ('description', django_quill.fields.QuillField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cours', verbose_name='Image')),
                ('plublish', models.DateTimeField(default=datetime.datetime(2022, 5, 21, 11, 11, 20, 109861, tzinfo=utc))),
                ('published', models.BooleanField(default=False, verbose_name='Publie')),
                ('statut', models.CharField(choices=[('en_ligne', 'En Ligne'), ('hors_ligne', 'Hors ligne')], default='hors_ligne', max_length=10, verbose_name='Statut')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_category', to='app_formation.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Cour',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200, verbose_name='niveau')),
            ],
            options={
                'verbose_name': 'Niveau',
                'verbose_name_plural': 'Niveaux',
            },
        ),
        migrations.CreateModel(
            name='Tutoriel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Slug')),
                ('description', django_quill.fields.QuillField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tutoriels', verbose_name='Poster')),
                ('url', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('published', models.BooleanField(default=False, verbose_name='Publie')),
                ('plublish', models.DateTimeField(default=datetime.datetime(2022, 5, 21, 11, 11, 20, 109861, tzinfo=utc))),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_category_tuto', to='app_formation.category', verbose_name='Category')),
                ('niveau', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_formation.niveau', verbose_name='niveau')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_user_tuto', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
            options={
                'verbose_name': 'Tutoriel',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Lecon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Slug')),
                ('description', django_quill.fields.QuillField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cours', verbose_name='Image')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('plublish', models.DateTimeField(default=datetime.datetime(2022, 5, 21, 11, 11, 20, 109861, tzinfo=utc))),
                ('published', models.BooleanField(default=False, verbose_name='Publie')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('cours', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_cours', to='app_formation.cours', verbose_name='Cours')),
            ],
            options={
                'verbose_name': 'Lecon',
            },
        ),
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_formation.niveau', verbose_name='niveau'),
        ),
        migrations.AddField(
            model_name='cours',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_user', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
    ]
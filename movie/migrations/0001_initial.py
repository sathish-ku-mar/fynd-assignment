# Generated by Django 3.1 on 2020-08-15 12:09

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='The name of the move', max_length=200)),
                ('director', models.CharField(help_text='A person name who controls the making of a movie', max_length=200)),
                ('genre', django_mysql.models.ListTextField(models.CharField(max_length=100), help_text='The category of the movie', size=100)),
                ('popularity', models.FloatField(help_text='How much people liked the movie')),
                ('imdb_score', models.FloatField(help_text='Users to rate films on a scale of one to ten')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': 'movie',
                'ordering': ['-id'],
                'get_latest_by': '-created_at',
            },
        ),
    ]
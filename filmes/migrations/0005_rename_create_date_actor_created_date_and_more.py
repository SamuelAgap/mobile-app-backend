# Generated by Django 4.2.4 on 2023-08-12 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0004_alter_actor_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='create_date',
            new_name='created_date',
        ),
    ]

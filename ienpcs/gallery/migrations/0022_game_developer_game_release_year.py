# Generated by Django 5.0.1 on 2024-01-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0021_rename_title_screen_320_game_title_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='release_year',
            field=models.SmallIntegerField(default=-1),
            preserve_default=False,
        ),
    ]

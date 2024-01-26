# Generated by Django 5.0.1 on 2024-01-26 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.character'),
            preserve_default=False,
        ),
    ]

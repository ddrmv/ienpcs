# Generated by Django 5.0.1 on 2024-01-26 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_npc_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='npc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.character'),
        ),
    ]
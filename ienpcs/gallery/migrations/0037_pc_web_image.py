# Generated by Django 5.0.1 on 2024-02-05 13:05

import gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0036_alter_slot_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='web_image',
            field=models.ImageField(blank=True, null=True, upload_to=gallery.models.pc_portrait_path),
        ),
    ]

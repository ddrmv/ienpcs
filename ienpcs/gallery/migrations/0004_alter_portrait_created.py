# Generated by Django 5.0.1 on 2024-01-23 13:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_portrait_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]

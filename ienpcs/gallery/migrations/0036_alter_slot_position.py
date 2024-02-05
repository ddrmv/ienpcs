# Generated by Django 5.0.1 on 2024-02-05 00:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0035_party_party_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='position',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)]),
        ),
    ]
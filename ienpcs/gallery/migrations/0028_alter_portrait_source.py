# Generated by Django 5.0.1 on 2024-01-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0027_alter_link_options_alter_portrait_zip_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='source',
            field=models.URLField(blank=True, default=''),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0031_alter_pc_options_alter_party_npcs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='adnd_class',
            field=models.CharField(blank=True, default='Fighter', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='alignment',
            field=models.CharField(blank=True, default='True Neutral', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='race',
            field=models.CharField(blank=True, default='Human', max_length=20, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0037_pc_web_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='cha',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='npc',
            name='con',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='npc',
            name='dex',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='npc',
            name='int',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='npc',
            name='str',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='npc',
            name='str_percentile',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='npc',
            name='wis',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='pc',
            name='cha',
            field=models.SmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='con',
            field=models.SmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='dex',
            field=models.SmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='int',
            field=models.SmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='str',
            field=models.SmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='str_percentile',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='wis',
            field=models.SmallIntegerField(blank=True, default=10, null=True),
        ),
    ]

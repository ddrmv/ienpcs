# Generated by Django 5.0.1 on 2024-02-03 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0029_invitationcode'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npcs', models.ManyToManyField(to='gallery.npc')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adnd_class', models.CharField(blank=True, max_length=40, null=True)),
                ('race', models.CharField(blank=True, max_length=20, null=True)),
                ('alignment', models.CharField(blank=True, max_length=20, null=True)),
                ('str', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('str_percentile', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('dex', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('con', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('int', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('wis', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('cha', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.party')),
            ],
        ),
    ]

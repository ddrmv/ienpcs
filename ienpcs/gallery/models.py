import hashlib
import os

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def web_image_with_hash(instance, filename):
    path = "web_portraits"
    fname, dot, extension = filename.rpartition(".")
    file_hash = hashlib.sha1(instance.web_image.read()).hexdigest()
    format = fname + "_" + file_hash + dot + extension
    return os.path.join(path, format)


def zip_file_with_hash(instance, filename):
    path = "zip_file"
    fname, dot, extension = filename.rpartition(".")
    file_hash = hashlib.sha1(instance.zip_file.read()).hexdigest()
    format = fname + "_" + file_hash + dot + extension
    return os.path.join(path, format)


def char_portrait_with_hash(instance, filename):
    path = "chars"
    fname, dot, extension = filename.rpartition(".")
    file_hash = hashlib.sha1(instance.img_170.read()).hexdigest()
    format = fname + "_" + file_hash + dot + extension
    return os.path.join(path, format)


class Game(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=10)
    short_name = models.CharField(max_length=10)
    order = models.SmallIntegerField()
    title_screen = models.ImageField(upload_to="games", null=True)
    developer = models.CharField(max_length=100)
    release_year = models.SmallIntegerField()

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("order",)


class CharOrigin(models.TextChoices):
    OR = "OR", _("Original")
    MO = "MO", _("Mod")
    BE = "BE", _("Beamdog")


class PortraitOrigin(models.TextChoices):
    OR = "OR", _("Original")
    MO = "MO", _("Mod")
    BE = "BE", _("Beamdog")
    FA = "FA", _("Fanart")


class Character(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    origin = models.CharField(
        max_length=2, choices=CharOrigin.choices, default=CharOrigin.OR
    )
    img_170 = models.ImageField(upload_to=char_portrait_with_hash)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("name",)


class Npc(models.Model):
    class Alignment(models.TextChoices):
        CG = "CG", _("Chaotic Good")
        NG = "NG", _("Neutral Good")
        LG = "LG", _("Lawful Good")
        CN = "CN", _("Chaotic Neutral")
        TN = "TN", _("True Neutral")
        LN = "LN", _("Lawful Neutral")
        CE = "CE", _("Chaotic Evil")
        NE = "NE", _("Neutral Evil")
        LE = "LE", _("Lawful Evil")
        UN = "UN", _("Unknown")

    web_image = models.ImageField(upload_to=web_image_with_hash, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    game = models.ManyToManyField(Game, through="NpcInGame")
    name = models.CharField(max_length=100)
    admin_note = models.CharField(max_length=25, null=True, blank=True)
    adnd_class = models.CharField(max_length=25)
    race = models.CharField(max_length=20)
    alignment = models.CharField(
        max_length=2, choices=Alignment.choices, default=Alignment.UN
    )
    str = models.IntegerField()
    str_percentile = models.IntegerField(null=True, blank=True)
    dex = models.IntegerField()
    con = models.IntegerField()
    int = models.IntegerField()
    wis = models.IntegerField()
    cha = models.IntegerField()
    description = models.CharField(max_length=500, blank=True, default="")

    def __str__(self):
        return f"{self.name} ({self.admin_note})"

    class Meta:
        ordering = ("name",)


class Portrait(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.SET_NULL)
    origin = models.CharField(
        max_length=2, choices=PortraitOrigin.choices, default=PortraitOrigin.OR
    )
    description = models.CharField(max_length=200, blank=True, default="")
    source = models.CharField(max_length=100, blank=True, default="")
    created = models.DateTimeField(default=timezone.now, blank=True)
    web_image = models.ImageField(upload_to=web_image_with_hash)
    zip_file = models.FileField(upload_to=zip_file_with_hash)

    def __str__(self):
        return f"{self.character.name} - {self.description[:20]}"

    class Meta:
        ordering = ("-created",)


class NpcInGame(models.Model):
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    npc = models.ForeignKey(Npc, null=True, on_delete=models.SET_NULL)
    origin = models.CharField(
        max_length=2, choices=CharOrigin.choices, default=CharOrigin.OR
    )

    def __str__(self):
        return f"{self.npc}  -  {self.game}"

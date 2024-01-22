from django.db import models
from django.utils.translation import gettext_lazy as _


class Game(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=10)

    def __str__(self):
        return self.codename


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

    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    adnd_class = models.CharField(max_length=25)
    race = models.CharField(max_length=20)
    alignment = models.CharField(
        max_length=2, choices=Alignment.choices, default=Alignment.UN
    )
    str = models.IntegerField()
    str_percentile = models.IntegerField(null=True)
    dex = models.IntegerField()
    con = models.IntegerField()
    int = models.IntegerField()
    wis = models.IntegerField()
    cha = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

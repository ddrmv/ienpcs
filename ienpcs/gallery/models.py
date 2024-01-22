from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=10)

    def __str__(self):
        return self.codename

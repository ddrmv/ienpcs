from django.test import TestCase

from .models import Game

class GalleryModelTests(TestCase):
    def test_game_gets_created(self):
        name = "Baldur's Gate"
        codename = "bg1"
        game = Game(name=name, codename=codename)
        self.assertEqual(game.codename, codename)
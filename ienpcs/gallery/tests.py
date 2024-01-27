from django.test import TestCase

from .models import Game, Npc


class GameModelTests(TestCase):
    def test_game_gets_created(self):
        game = Game(name="Baldur's Gate", slug="bg1")
        self.assertEqual(game.slug, "bg1")


class NpcModelTests(TestCase):
    def test_create_npc(self):
        game = Game.objects.create(name="BG", slug="bg1")
        npc = Npc.objects.create(
            game=game,
            name="Edwin",
            adnd_class="Conjurer",
            race="Human",
            alignment="NE",
            str=9,
            str_percentile=None,
            dex=10,
            con=16,
            int=18,
            wis=9,
            cha=10,
            description="Edwin is a Wizard (Conjurer).",
        )
        self.assertEqual(npc.name, "Edwin")

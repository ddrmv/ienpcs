from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Game
from .validators import web_image_size


class GameModelTest(TestCase):
    def setUp(self):
        self.game1 = Game.objects.create(
            name="Test 1",
            slug="t1",
            short_name="T1",
            developer="Dev",
            release_year=2000,
            order=2,
        )
        self.game2 = Game.objects.create(
            name="Test 2",
            slug="t2",
            short_name="T2",
            developer="Dev",
            release_year=2000,
            order=1,
        )

    def test_ordering(self):
        games = Game.objects.all()
        self.assertEqual(games[0], self.game2)
        self.assertEqual(games[1], self.game1)


class GameListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        image = SimpleUploadedFile(
            name="test_image.jpg", content=b"", content_type="image/jpeg"
        )
        # Create 3 games for tests
        for game_id in range(3):
            Game.objects.create(
                name=f"Test Game {game_id}",
                slug=f"tg{game_id}",
                short_name=f"TG{game_id}",
                order=game_id,
                title_screen=image,
                developer="Dev",
                release_year=2000,
            )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("gallery:game_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery/game_list.html")

    def test_view_sets_correct_context_variable(self):
        response = self.client.get(reverse("gallery:game_list"))
        self.assertTrue("game_list" in response.context)

    def test_view_returns_all_games(self):
        response = self.client.get(reverse("gallery:game_list"))
        self.assertEqual(len(response.context["game_list"]), 3)

    def test_template_displays_game_list(self):
        response = self.client.get(reverse("gallery:game_list"))
        for game in response.context["game_list"]:
            self.assertContains(response, game.name)


class WebImageSizeValidatorTest(TestCase):
    def test_validator_raises_error_for_large_file(self):
        # Create a fake uploaded file that's too large 100 KB + 1 B
        large_image = SimpleUploadedFile(
            name="larger_than_100kb.jpg",
            content=b"x" * (100 * 1024 + 1),
            content_type="image/jpeg",
        )
        with self.assertRaises(ValidationError):
            web_image_size(large_image)

    def test_validator_does_not_raise_error_for_small_file(self):
        # Create a fake uploaded file that's small enough
        small_image = SimpleUploadedFile(
            name="exactly_100kb.jpg",
            content=b"x" * (100 * 1024),
            content_type="image/jpeg",
        )
        try:
            web_image_size(small_image)
        except ValidationError:
            self.fail("web_image_size raised ValidationError unexpectedly")

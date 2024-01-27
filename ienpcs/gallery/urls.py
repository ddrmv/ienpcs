from django.urls import path

from . import views

urlpatterns = [
    path("", views.GameListView.as_view(), name="game_list"),
    path("games/", views.GameListView.as_view(), name="game_list"),
    path("links/", views.link_list, name="link_list"),
    path("about/", views.about, name="about"),
    path("characters/", views.CharacterListView.as_view(), name="character_list"),
    path("game/<slug:slug>", views.game_detail, name="game_detail"),
    path("toggle_theme", views.toggle_theme, name="toggle_theme"),
]

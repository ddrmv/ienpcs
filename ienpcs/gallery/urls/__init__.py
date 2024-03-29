from django.urls import path

from .. import views
from .party_urls import urlpatterns as party_urls

app_name = "gallery"

# This is the main section, party management related urls are added from party_urls
urlpatterns = [
    path("", views.GameListView.as_view(), name="index"),
    path("games/", views.GameListView.as_view(), name="game_list"),
    path("game/<slug:slug>", views.game_detail, name="game_detail"),
    path("characters/", views.CharacterListView.as_view(), name="character_list"),
    path("character/<slug:slug>", views.character_detail, name="character_detail"),
    path("links/", views.LinkListView.as_view(), name="link_list"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("toggle_theme", views.toggle_theme, name="toggle_theme"),
]

urlpatterns += party_urls

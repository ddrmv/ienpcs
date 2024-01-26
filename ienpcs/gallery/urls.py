from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("game/<slug:slug>", views.game_detail, name="game-detail"),
    path("toggle_theme", views.toggle_theme, name="toggle_theme"),
]

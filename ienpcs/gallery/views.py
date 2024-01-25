# from django.shortcuts import render
from django.views import generic

from .models import Game


class IndexView(generic.ListView):
    template_name = "gallery/index.html"
    context_object_name = "game_list"
    queryset = Game.objects.all()


class GameDetailView(generic.DetailView):
    template_name = "gallery/game_detail.html"
    model = Game
    slug_field = "codename"

# from django.shortcuts import render
from django.views import generic

from .models import Game


class IndexView(generic.ListView):
    template_name = "gallery/index.html"
    context_object_name = "game_list"
    queryset = Game.objects.all()

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Game, NpcInGame


class GameListView(generic.ListView):
    template_name = "gallery/game_list.html"
    context_object_name = "game_list"
    queryset = Game.objects.all()


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    unique_origins = ["OR", "BE", "MO"]
    origin_map = {"OR": "Original", "BE": "Beamdog", "MO": "Mods"}
    origin_dict = {}
    for origin in unique_origins:
        origin_dict[origin_map[origin]] = NpcInGame.objects.filter(
            game=game, origin=origin
        ).order_by("npc__name")
        if not origin_dict[origin_map[origin]]:
            del origin_dict[origin_map[origin]]
    return render(
        request, "gallery/game_detail.html", {"game": game, "origin_dict": origin_dict}
    )


class CharacterListView(generic.ListView):
    template_name = "gallery/character_list.html"
    context_object_name = "character_list"
    queryset = Game.objects.all()


def link_list(request):
    link_list_dict = {"link1": "placeholder1", "link2": "placeholder2"}
    context = {"link_list_dict": link_list_dict}
    return render(request, "gallery/link_list.html", context)


def about(request):
    return render(request, "gallery/about.html", {})


def toggle_theme(request):
    if request.session.get("theme", "light") == "dark":
        request.session["theme"] = "iight"
    else:
        request.session["theme"] = "dark"
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

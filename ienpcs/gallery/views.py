from django.http import HttpResponseRedirect
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


def toggle_theme(request):
    if request.session.get("theme", "light") == "dark":
        request.session["theme"] = "iight"
    else:
        request.session["theme"] = "dark"
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

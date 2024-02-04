from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import generic

from .forms import CreatePcForm, SignUpForm
from .models import Character, Game, InvitationCode, Link, Npc, NpcInGame, Party, Pc

MAX_NPCS_PER_PARTY = 20


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
    queryset = Character.objects.all()


def character_detail(request, slug):
    character = get_object_or_404(Character, slug=slug)
    npcs = character.npc_set.all()
    for npc in npcs:
        npc.npc_in_games = NpcInGame.objects.filter(npc=npc)
    return render(
        request, "gallery/character_detail.html", {"character": character, "npcs": npcs}
    )


class LinkListView(generic.ListView):
    template_name = "gallery/link_list.html"
    context_object_name = "links"
    queryset = Link.objects.all()


def about(request):
    return render(request, "gallery/about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect("game_list")
        else:
            messages.error(request, "Error: Login unsuccessful.")
            return redirect("login")
    else:
        return render(request, "gallery/login.html", {})


def logout_user(request):
    if request.user.is_authenticated:
        theme = request.session.get("theme", "light")
        logout(request)
        request.session["theme"] = theme
        messages.success(request, "You have successfully logged out!")
        return redirect("game_list")
    else:
        messages.error(request, "Error: You are not currently logged in!")
        return redirect("login")


def register_user(request):
    if request.user.is_authenticated:
        messages.error(request, "Error: You are already registered and logged in!")
        return redirect("index")

    if request.method != "POST":
        form = SignUpForm()
        return render(request, "gallery/register.html", {"form": form})

    # else (request.method == "POST")
    form = SignUpForm(request.POST)
    if form.is_valid():
        # Check invitation is valid and not used over limit
        invitation_code_input = form.cleaned_data["invitation_code"]
        try:
            InvitationCode.objects.get(code=invitation_code_input)
        except InvitationCode.DoesNotExist:
            messages.error(request, "Invalid invitation code.")
            form = SignUpForm()
            return render(request, "gallery/register.html", {"form": form})
        invitation = InvitationCode.objects.get(code=invitation_code_input)
        if invitation.times_used >= invitation.max_uses:
            messages.error(
                request,
                "The invitation code has been used too many times, please request another.",
            )
            form = SignUpForm()
            return render(request, "gallery/register.html", {"form": form})

        # Update times invitation has been used
        invitation.times_used += 1
        invitation.last_used = timezone.now()
        invitation.save()

        # Save new user in database and log in
        user = form.save()
        Party.objects.create(user=user)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)
        theme = request.session.get("theme", "light")
        login(request, user)
        request.session["theme"] = theme
        messages.success(
            request, "You have successfully registered and have been logged in."
        )
        return redirect("index")
    else:
        return render(request, "gallery/register.html", {"form": form})


def party_detail(request):
    context = {}
    if request.user.is_authenticated:
        party = Party.objects.get(user=request.user)
        npcs = party.npcs.all()
        pcs = Pc.objects.filter(party=party)
        context["npcs"] = npcs
        context["pcs"] = pcs
    return render(request, "gallery/party_detail.html", context)


def party_add_npc(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to add NPCs.")
    else:
        party = Party.objects.get(user=request.user)
        npc = Npc.objects.get(id=id)
        if party.npcs.count() >= MAX_NPCS_PER_PARTY:
            messages.error(request, "Already at maximum number of NPCs in Party.")
        elif party.npcs.filter(id=npc.id).exists():
            messages.error(request, "NPC already in Party.")
        else:
            party.npcs.add(npc)
            messages.success(request, "NPC added to Party!")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def party_create_pc(request):
    if not request.user.is_authenticated:
        messages.error(request, "Error: You need to be logged in to Add PC.")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    if request.method != "POST":
        form = CreatePcForm()
        return render(request, "gallery/party_create_pc.html", {"form": form})

    # else (request.method == "POST")
    form = CreatePcForm(request.POST)
    if form.is_valid():
        party = Party.objects.get(user=request.user)
        pc = form.save(commit=False)
        pc.party = party
        pc.save()
        messages.success(request, "PC has been created.")
        return redirect("party_detail")
    else:
        return render(request, "gallery/party_create_pc.html", {"form": form})


def party_delete_pc(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to delete PCs.")
    else:
        party = Party.objects.get(user=request.user)
        pcs = Pc.objects.filter(party=party)
        if not pcs.filter(id=id).exists():
            messages.error(request, "You cannot delete this PC.")
        else:
            pc = Pc.objects.get(id=id)
            pc.delete()
            messages.success(request, "PC deleted!")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def party_update_pc(request, id):
    party = Party.objects.get(user=request.user)
    current_pc = get_object_or_404(Pc, id=id, party=party)

    if request.method == "POST":
        form = CreatePcForm(request.POST, instance=current_pc)
        if form.is_valid():
            form.save()
            messages.success(request, "PC updated!")
            return redirect("party_detail")
    else:
        form = CreatePcForm(instance=current_pc)

    return render(request, "gallery/party_update_pc.html", {"form": form, "pc_id": id})


def party_remove_npc(request, id):
    if request.user.is_authenticated:
        party = Party.objects.get(user=request.user)
        npc = Npc.objects.get(id=id)
        party.npcs.remove(npc)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def toggle_theme(request):
    if request.session.get("theme", "light") == "dark":
        request.session["theme"] = "iight"
    else:
        request.session["theme"] = "dark"
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

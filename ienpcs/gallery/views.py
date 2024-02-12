from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import generic

from .forms import AuthenticateUserForm, ContactForm, CreatePcForm, SignUpForm
from .models import (
    Character,
    Game,
    InvitationCode,
    Link,
    Npc,
    NpcInGame,
    Party,
    Pc,
    Slot,
)

MAX_NPCS_PER_PARTY = 20  # Maximum number of Npcs shortlisted on party page
MAX_PCS_PER_PARTY = 10  # Maximum number of Pcs shortlisted on party page


class GameListView(generic.ListView):
    """Lists all admin-created Game instances."""

    template_name = "gallery/game_list.html"
    context_object_name = "game_list"
    queryset = Game.objects.all()


def game_detail(request, slug):
    """Handles per-Game data, has list of Npc, grouped by origin."""
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
    """Lists all admin-created Character instances."""

    template_name = "gallery/character_list.html"
    context_object_name = "character_list"
    queryset = Character.objects.all()


def character_detail(request, slug):
    """Handles per-Character data, has list of Npc, grouped by origin.

    Prefetches the Games in which each of the Npcs for the Character appear.
    """

    character = get_object_or_404(Character, slug=slug)
    npcs = character.npc_set.prefetch_related("game").all()
    return render(
        request, "gallery/character_detail.html", {"character": character, "npcs": npcs}
    )


class LinkListView(generic.ListView):
    """Lists all admin-created Link instances."""

    template_name = "gallery/link_list.html"
    context_object_name = "links"
    queryset = Link.objects.all()


# Contact form inside About page
# SMTP needs to be configured for the form to function, otherwise shows an Error
def about(request):
    """Handles About page, with Contact form.

    Contact form needs to be set up with email provider to function.
    If email provide isn't configured, it throws an error that is haldled.
    """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(
                    "Subject: IENPCs contact form message",
                    f"[name]: {name} [email]: ({email}) says:\n\n{message}",
                    "example@example.com",  # Site origin email
                    ["example@example.com"],  # Site admin email
                )
                messages.success(request, "Email sent successfully!")
                return redirect("gallery:about")
            except Exception as e:
                messages.error(request, f"Error: {e}")
                return redirect("gallery:about")
    else:
        form = ContactForm()

    return render(request, "gallery/about.html", {"form": form})


def login_user(request):
    """Handles user/admin login."""
    if request.method == "POST":
        form = AuthenticateUserForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "You have successfully logged in!")
            return redirect("gallery:game_list")
        else:
            messages.error(request, "Error: Login unsuccessful.")
    else:
        form = AuthenticateUserForm()

    return render(request, "gallery/login.html", {"form": form})


@login_required
def logout_user(request):
    """Handles user logout, redirects to index page."""
    theme = request.session.get("theme", "light")
    logout(request)
    request.session["theme"] = theme
    messages.success(request, "You have successfully logged out!")
    return redirect("gallery:index")


def register_user(request):
    """Handles user registration.

    Redirects to itself until form is valid, then updates Dark/Light theme and
    redirects to the index page.
    """

    if request.user.is_authenticated:
        messages.error(request, "Error: You are already registered and logged in!")
        return redirect("gallery:index")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Check invitation is valid and not used over limit
            invite_code = form.cleaned_data["invitation_code"]
            try:
                InvitationCode.objects.get(code=invite_code)
            except InvitationCode.DoesNotExist:
                messages.error(request, "Invalid invitation code.")
                return render(request, "gallery/register.html", {"form": form})

            invitation = InvitationCode.objects.get(code=invite_code)
            if invitation.times_used >= invitation.max_uses:
                messages.error(request, "Invite code expired please request another.")
                return render(request, "gallery/register.html", {"form": form})

            # Update times invitation has been used
            invitation.times_used += 1
            invitation.last_used = timezone.now()
            invitation.save()

            # Save new user in database and log in
            user = form.save()
            Party.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration and login successful!")
            return redirect("gallery:index")
    else:
        form = SignUpForm()

    return render(request, "gallery/register.html", {"form": form})


def party_detail(request):
    """Handles party management main page.

    If user is logged in, allows party management, otherwise shows
    empty tables and no slots.
    """

    context = {}
    if request.user.is_authenticated:
        party = Party.objects.get(user=request.user)
        npcs = party.npcs.all()
        pcs = Pc.objects.filter(party=party)
        slots = Slot.objects.filter(party=party)[: party.party_size]
        context = {
            "npcs": npcs,
            "pcs": pcs,
            "slots": slots,
        }
    return render(request, "gallery/party_detail.html", context)


@login_required
def party_add_npc(request, id):
    """Handles adding an Npc to the party shortlist, redirects to same page."""
    party = Party.objects.get(user=request.user)
    npc = get_object_or_404(Npc, id=id)

    if party.npcs.count() >= MAX_NPCS_PER_PARTY:
        messages.error(request, "Already at maximum number of NPCs in Party.")
    elif party.npcs.filter(id=npc.id).exists():
        messages.error(request, "NPC already in Party.")
    else:
        party.npcs.add(npc)
        messages.success(request, "NPC added to Party!")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def party_create_pc(request):
    """Handles craeting a Pc by user, redirects to party page."""
    party = get_object_or_404(Party, user=request.user)
    if party.pc_set.count() >= MAX_PCS_PER_PARTY:
        messages.error(request, f"The party already has {MAX_PCS_PER_PARTY} PCs.")
        return redirect("gallery:party_detail")

    if request.method == "POST":
        form = CreatePcForm(request.POST, request.FILES, instance=Pc(party=party))
        if form.is_valid():
            form.save()
            messages.success(request, "PC has been created.")
            return redirect("gallery:party_detail")
    else:
        form = CreatePcForm()

    return render(request, "gallery/party_create_pc.html", {"form": form})


@login_required
def party_delete_pc(request, id):
    """Handles deleting a user-created Pc, redirects back to same (party) page."""
    party = Party.objects.get(user=request.user)
    pc = get_object_or_404(Pc, id=id, party=party)
    pc.delete()
    messages.success(request, "PC deleted!")
    return redirect("gallery:party_detail")


@login_required
def party_update_pc(request, id):
    """Handles updating/modifying a user-created Pc, redirects back to party page."""
    party = Party.objects.get(user=request.user)
    current_pc = get_object_or_404(Pc, id=id, party=party)

    if request.method == "POST":
        form = CreatePcForm(request.POST, request.FILES, instance=current_pc)
        if form.is_valid():
            form.save()
            messages.success(request, "PC updated!")
            return redirect("gallery:party_detail")
    else:
        form = CreatePcForm(instance=current_pc)

    return render(request, "gallery/party_update_pc.html", {"form": form, "pc_id": id})


@login_required
def party_remove_npc(request, id):
    """Handles removing Npc from Party shortlist, redirects back to same (party) page."""
    party = Party.objects.get(user=request.user)
    npc = get_object_or_404(Npc, id=id)
    party.npcs.remove(npc)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def party_set_size(request, party_size):
    """Handles resizing the party, changing the number of slots.

    Upon setting the slot size to less than maximum,
    clears all not-shown extra slots.
    """

    party = Party.objects.get(user=request.user)
    party.party_size = party_size
    party.save()
    party.slot_set.filter(position__gt=party_size).update(
        object_id=None, content_type=None
    )
    return redirect("gallery:party_detail")


@login_required
def party_slot_clear(request, position):
    """Handles clearing a slot from Npc/Pc."""
    party = Party.objects.get(user=request.user)
    slot = party.slot_set.get(position=position)
    slot.object_id = None
    slot.content_type = None
    slot.save()
    return redirect("gallery:party_detail")


@login_required
def party_slot_set_npc(request, position, id):
    """Sets an Npc from the party shortlist to the slot at position."""
    party = Party.objects.get(user=request.user)
    slot = party.slot_set.get(position=position)
    slot.object_id = id
    slot.content_type = ContentType.objects.get_for_model(Npc)
    slot.save()
    return redirect("gallery:party_detail")


@login_required
def party_slot_set_pc(request, position, id):
    """Sets an Pc from the party shortlist to the slot at position."""
    party = Party.objects.get(user=request.user)
    slot = party.slot_set.get(position=position)
    get_object_or_404(Pc, party=party, id=id)
    slot.object_id = id
    slot.content_type = ContentType.objects.get_for_model(Pc)
    slot.save()
    return redirect("gallery:party_detail")


@login_required
def party_slot_swap_left(request, position):
    """Swaps the slot at position with one to the left, checks one exists."""
    party = Party.objects.get(user=request.user)
    if position <= party.party_size and position > 1:
        slot = party.slot_set.get(position=position)
        slot_on_left = party.slot_set.get(position=position - 1)
        slot_on_left.position, slot.position = slot.position, slot_on_left.position
        slot.save()
        slot_on_left.save()
    return redirect("gallery:party_detail")


@login_required
def party_slot_swap_right(request, position):
    """Swaps the slot at position with one to the right, checks one exists."""
    party = Party.objects.get(user=request.user)
    if position <= party.party_size - 1 and position > 0:
        slot = party.slot_set.get(position=position)
        slot_on_right = party.slot_set.get(position=position + 1)
        slot_on_right.position, slot.position = slot.position, slot_on_right.position
        slot.save()
        slot_on_right.save()
    return redirect("gallery:party_detail")


def toggle_theme(request):
    """Handles the Dark/Light button for website Theme, redirects back to caller page."""
    theme = "dark" if request.session.get("theme", "light") == "light" else "light"
    request.session["theme"] = theme
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

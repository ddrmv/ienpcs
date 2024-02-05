from django.urls import path

from . import views

urlpatterns = [
    path("", views.GameListView.as_view(), name="index"),
    path("games/", views.GameListView.as_view(), name="game_list"),
    path("game/<slug:slug>", views.game_detail, name="game_detail"),
    path("characters/", views.CharacterListView.as_view(), name="character_list"),
    path("character/<slug:slug>", views.character_detail, name="character_detail"),
    path("party/", views.party_detail, name="party_detail"),
    path("party_add_npc/<int:id>/", views.party_add_npc, name="party_add_npc"),
    path("party_create_pc/", views.party_create_pc, name="party_create_pc"),
    path("party_delete_pc/<int:id>/", views.party_delete_pc, name="party_delete_pc"),
    path("party_update_pc/<int:id>/", views.party_update_pc, name="party_update_pc"),
    path("party_remove_npc/<int:id>/", views.party_remove_npc, name="party_remove_npc"),
    path(
        "party/set_size/<int:party_size>/", views.party_set_size, name="party_set_size"
    ),
    path(
        "party/slot_clear/<int:position>/",
        views.party_slot_clear,
        name="party_slot_clear",
    ),
    path(
        "party/slot_set_npc/<int:position>/<int:id>",
        views.party_slot_set_npc,
        name="party_slot_set_npc",
    ),
    path(
        "party/slot_set_pc/<int:position>/<int:id>",
        views.party_slot_set_pc,
        name="party_slot_set_pc",
    ),
    path(
        "party/slot_swap_left/<int:position>/",
        views.party_slot_swap_left,
        name="party_slot_swap_left",
    ),
    path(
        "party/slot_swap_right/<int:position>/",
        views.party_slot_swap_right,
        name="party_slot_swap_right",
    ),
    path("links/", views.LinkListView.as_view(), name="link_list"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("toggle_theme", views.toggle_theme, name="toggle_theme"),
]

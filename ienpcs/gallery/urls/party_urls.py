from django.urls import path

from .. import views

urlpatterns = [
    path("party/", views.party_detail, name="party_detail"),
    path("party/add_npc/<int:id>/", views.party_add_npc, name="party_add_npc"),
    path("party/create_pc/", views.party_create_pc, name="party_create_pc"),
    path("party/delete_pc/<int:id>/", views.party_delete_pc, name="party_delete_pc"),
    path("party/update_pc/<int:id>/", views.party_update_pc, name="party_update_pc"),
    path("party/remove_npc/<int:id>/", views.party_remove_npc, name="party_remove_npc"),
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
]

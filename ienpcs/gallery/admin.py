from django.contrib import admin

# All models, each with an admin.ModelAdmin class, are registered with admin.site
from .models import (
    Character,
    Game,
    InvitationCode,
    Link,
    Npc,
    NpcInGame,
    Party,
    Pc,
    Portrait,
    Slot,
)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "origin", "turncated_description"]
    list_filter = ["origin"]
    search_fields = ["name"]

    def turncated_description(self, obj):
        return obj.description[:50]


class GameAdmin(admin.ModelAdmin):
    list_display = [
        "slug",
        "short_name",
        "name",
        "order",
        "title_screen",
        "developer",
        "release_year",
    ]


class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "note",
        "in_use",
        "max_uses",
        "times_used",
        "added",
        "last_used",
    ]
    list_filter = ["in_use"]
    search_fields = ["note"]


class LinkAdmin(admin.ModelAdmin):
    list_display = [
        "description",
        "url",
    ]


class NpcAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "web_image",
                    "character",
                    "name",
                    "admin_note",
                    "description",
                ]
            },
        ),
        (
            "ADnD Stats",
            {
                "fields": [
                    "adnd_class",
                    "race",
                    "alignment",
                    "str",
                    "str_percentile",
                    "dex",
                    "con",
                    "int",
                    "wis",
                    "cha",
                ],
                "classes": ["collapse"],
            },
        ),
    ]
    list_display = ["name", "admin_note"]
    search_fields = ["name"]


class NpcInGameAdmin(admin.ModelAdmin):
    fields = ["npc", "game", "origin"]
    list_display = ["npc", "game", "origin"]
    list_filter = ["game__slug"]
    search_fields = ["npc__name"]


class PartyAdmin(admin.ModelAdmin):
    list_display = ["user"]


class PcAdmin(admin.ModelAdmin):
    list_display = ["party", "name", "adnd_class", "race", "alignment"]
    search_fields = ["name"]


class PortraitAdmin(admin.ModelAdmin):
    list_display = [
        "character",
        "origin",
        "turncated_description",
        "source",
        "created",
        "web_image",
    ]
    list_filter = ["origin"]
    search_fields = ["character__name"]

    def turncated_description(self, obj):
        return obj.description[:20]


class SlotAdmin(admin.ModelAdmin):
    list_display = [
        "party",
        "position",
        "content_type",
        "object_id",
        "content_object",
    ]


admin.site.register(Character, CharacterAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(InvitationCode, InvitationCodeAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Npc, NpcAdmin)
admin.site.register(NpcInGame, NpcInGameAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Pc, PcAdmin)
admin.site.register(Portrait, PortraitAdmin)
admin.site.register(Slot, SlotAdmin)

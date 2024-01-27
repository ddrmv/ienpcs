from django.contrib import admin

from .models import Character, Game, Npc, NpcInGame, Portrait


class NpcInGameAdmin(admin.ModelAdmin):
    fields = ["npc", "game", "origin"]
    list_display = ["npc", "game", "origin"]
    list_filter = ["game__slug"]
    search_fields = ["npc__name"]


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


admin.site.register(Game)
admin.site.register(Npc, NpcAdmin)
admin.site.register(NpcInGame, NpcInGameAdmin)
admin.site.register(Portrait)
admin.site.register(Character)

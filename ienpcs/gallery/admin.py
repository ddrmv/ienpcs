from django.contrib import admin

from .models import Character, Game, Npc, NpcInGame, Portrait


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


admin.site.register(Game, GameAdmin)
admin.site.register(Npc, NpcAdmin)
admin.site.register(NpcInGame, NpcInGameAdmin)
admin.site.register(Portrait, PortraitAdmin)
admin.site.register(Character, CharacterAdmin)

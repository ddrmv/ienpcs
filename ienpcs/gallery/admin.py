from django.contrib import admin

from .models import Game, Npc, NpcInGame, Portrait

admin.site.register(Game)
admin.site.register(Npc)
admin.site.register(NpcInGame)
admin.site.register(Portrait)

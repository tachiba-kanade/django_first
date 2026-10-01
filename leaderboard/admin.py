from django.contrib import admin

from .models import Player, Game, Score

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Score)
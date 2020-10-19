from django.contrib import admin

# Register your models here.
from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Person)

from django.db import models

from django102.models.player import Player


class GameManager(models.Manager):
    def all_with_players_count(self):
        return self.all().annotate(players_count = models.Count('players'))


class Game(models.Model):
    objects = GameManager()

    EASY = 0
    MEDIUM = 1
    HARD = 2

    DIFICULTY_LEVELS_CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )
    name = models.CharField(max_length=30, blank=False, default='')
    level_of_difficulty = models.IntegerField(
        blank=False,
        choices=DIFICULTY_LEVELS_CHOICES,
        default=MEDIUM,
    )
    players = models.ManyToManyField(Player)

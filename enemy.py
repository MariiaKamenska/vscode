import random

from config import difficulty_chart

class Enemy:

    def __init__(
        self,
        name,
        player,
        base_health=(4, 7),
        base_attack=(0, 5)
    ):

        self.name = name
        self.player = player

        self.max_health = int(
            random.randint(*base_health)
            * difficulty_chart[player.difficulty]['enemy']['hp']
        )

        self._health = self.max_health

        self.base_attack = base_attack

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    def is_dead(self):
        return self.health <= 0

    def attack(self):

        min_attack = int(
            (self.base_attack[0] + self.player.level)
            * difficulty_chart[self.player.difficulty]['enemy']['attack']
        )

        max_attack = int(
            (self.base_attack[1] + self.player.level * 2)
            * difficulty_chart[self.player.difficulty]['enemy']['attack']
        )

        return random.randint(min_attack, max_attack)
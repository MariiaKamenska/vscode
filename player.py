import random
import time
from config import difficulty_chart

class Player:
    def __init__(
        self,
        name,
        race,
        difficulty,
        base_health=12,
        attack_range=(0, 5),
        gold=0,
        strength = 8,
        dexterity = 8, 
        intelligence = 8,
        charisma = 8,
        wisdom = 8,
        constitution = 8,
    ):
        self.name = name
        self.race = race
        self.difficulty = difficulty
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.charisma = charisma
        self.constitution = constitution
        self.wisdom = wisdom


        self.max_health = int(
            base_health *
            difficulty_chart[difficulty]['player']['hp']
        )

        self._health = self.max_health

        self.attack_range = attack_range
        self.gold = gold

        self.level = 1
        self.xp = 0
        self.next_level_xp = 100

        self.lawful = 0
        self.chaotic = 0
        self.good = 0
        self.evil = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self.max_health))

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        min_attack = int(
            (self.attack_range[0] + self.level)
            * difficulty_chart[self.difficulty]['player']['attack']
        )

        max_attack = int(
            (self.attack_range[1] + self.level * 2)
            * difficulty_chart[self.difficulty]['player']['attack']
        )
        return random.randint(min_attack, max_attack)

    def restore_health(self):
        self.health = self.max_health
        print(
            f"{self.name} restores "
            f"health to {self.health}/{self.max_health}."
        )

    def gain_gold(self, amount):
        scaled = int(
            amount *
            difficulty_chart[self.difficulty]['player']['gold_gain']
        )
        self.gold += scaled
        print(f"{self.name} gains {scaled} gold.")

    def gain_xp(self, amount):
        scaled = int(
            amount *
            difficulty_chart[self.difficulty]['player']['xp_gain']
        )
        self.xp += scaled
        print(f"{self.name} gains {scaled} XP.")
        while self.xp >= self.next_level_xp:
            self.xp -= self.next_level_xp
            self.level += 1
            hp_gain = int(5 * (self.level ** 0.5))
            self.max_health += hp_gain
            print(f"{self.name} reached level {self.level}!")
            self.next_level_xp = int(self.next_level_xp * 1.5)
            time.sleep(1)
import random
import sys
import time

difficulty_chart = {
    "Easy": {
        'player': {'hp': 1, 'attack': 1, 'xp_gain': 0.7, 'gold_gain': 1.3},
        'enemy': {'hp': 1, 'attack': 1}
    },
    "Normal": {
        'player': {'hp': 0.8, 'attack': 1.1, 'xp_gain': 1, 'gold_gain': 1},
        'enemy': {'hp': 1.2, 'attack': 1.2}
    },
    "Hard": {
        'player': {'hp': 0.72, 'attack': 1.2, 'xp_gain': 1.3, 'gold_gain': 0.8},
        'enemy': {'hp': 1.4, 'attack': 1.2}
    },
    "Masochist": {
        'player': {'hp': 0.65, 'attack': 1.4, 'xp_gain': 1.6, 'gold_gain': 0.6},
        'enemy': {'hp': 2, 'attack': 1.6}
    }

}

class Player:
    def __init__(self, name, race, base_health=12, attack_range=(0, 5), gold=0, 
                 lawful=0, chaotic=0, good=0, evil=0, level=1, xp=0, difficulty = 'Normal'):
        self.name = name
        self.race = race
        self.difficulty = difficulty
        self.max_health = int(base_health * difficulty_chart[difficulty]['player']['hp'])
        self._health = self.max_health
        self.attack_range = attack_range
        self.gold = gold
        self.level = level
        self.xp = xp
        self.next_level_xp = 100

        self.lawful = lawful
        self.chaotic = chaotic
        self.good = good
        self.evil = evil

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self.max_health))

    def is_dead(self):
        return self._health <= 0

    def attack(self):
        min_attack = int((self.attack_range[0] + self.level) * difficulty_chart[self.difficulty]['player']['attack'])
        max_attack = int((self.attack_range[1] + self.level * 2) * difficulty_chart[self.difficulty]['player']['attack'])
        return random.randint(min_attack, max_attack)

    def restore_health(self):
        self.health = self.max_health
        print(f"{self.name} rests and restores health to {self.health}/{self.max_health} HP.")

    def gain_gold(self, amount):
        scaled_amount = int(amount * difficulty_chart[self.difficulty]['player']['gold_gain'])
        self.gold += scaled_amount
        print(f"{self.name} acquires {scaled_amount} gold. Total gold: {self.gold}.")

    def update_alignment(self, lawful_delta=0, chaotic_delta=0, good_delta=0, evil_delta=0):
        self.lawful += lawful_delta
        self.chaotic += chaotic_delta
        self.good += good_delta
        self.evil += evil_delta
        print(f"Alignment updated: Lawful {self.lawful}, Chaotic {self.chaotic}, "
              f"Good {self.good}, Evil {self.evil}.")

    def gain_xp(self, amount):
        scaled_xp = int(amount * difficulty_chart[self.difficulty]['player']['xp_gain'])
        self.xp += scaled_xp
        print(f"{self.name} gains {scaled_xp} XP. Total XP: {self.xp}.")
        while self.xp >= self.next_level_xp:
            self.xp -= self.next_level_xp
            self.level += 1
            health_increase = int(5 * (self.level ** 0.5))
            self.max_health += health_increase
            time.sleep(1)
            print(f"{self.name} leveled up! Current level {self.level}, "
                  f"max health {self.max_health} HP.")
            time.sleep(1)
            self.next_level_xp = int(self.next_level_xp * 1.5)
            print(f"XP needed for next level: {self.next_level_xp}")


class Enemy:
    def __init__(self, name, player, base_health=(4, 7), base_attack=(0, 5)):
        self.name = name
        self.player = player
        self.max_health = int(random.randint(*base_health) * difficulty_chart[player.difficulty]["enemy"]["hp"])
        self._health = self.max_health
        self.base_attack = base_attack

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = max(0, value)

    def is_dead(self):
        return self._health <= 0

    def attack(self):
        min_attack = int((self.base_attack[0] + self.player.level) * difficulty_chart[self.player.difficulty]['enemy']['attack'])
        max_attack = int((self.base_attack[1] + self.player.level * 2) * difficulty_chart[self.player.difficulty]['enemy']['attack'])
        return random.randint(min_attack, max_attack)



print("Hello! Choose the difficulty:\n1-Easy, 2-Normal, 3-Hard, 4-Masochist")
diff_choice = int(input())
diff_map = {1:'Easy', 2:'Normal', 3:'Hard', 4:'Masochist'}
difficulty = diff_map.get(diff_choice)

name = str(input('Enter your name: '))
time.sleep(0.5)
print(f"Nice name for our main character - {name}!")
race_choice = int(input('Enter your race\n1-Human, 2-Orc, 3-Tiefling, 4-Dragonborn, 5-Elf'))
race_map = {1:"Human",2:"Orc",3:"Tiefling",4:"Dragonborn",5:"Elf"}
race = race_map.get(race_choice)
gold = random.randint(0, 45)

player = Player(name, race, health=10, attack_range=(0, 6), gold=gold)
print(f"{player.name}, the {player.race}, starts with {player.health} HP and {player.gold} gold on {difficulty} difficulty.")

# city = input("Enter your city: ")
# time.sleep(0.5)
# print(f'{player.name}, the {player.race} from {city}. Wondrous!')
# time.sleep(2)
time.sleep(6)
print("You begin as a Neutral character, but you will have all the freedom "
      "to bring changes as the story progresses.")
time.sleep(6)
print("Looks like you've stumbled upon an enemy...")
time.sleep(2)

enemies = ["Ogre", "Goblin", "Bandit", "Skeleton", "Dire Wolf", "Troll", "Drow"]
enemy_name = random.choice(enemies)
enemy = Enemy(enemy_name, player, base_health=(2, 5), base_attack=(0, 5))

print(f"{enemy.name} blocks your path! Careful now!")
time.sleep(0.5)
print(f"{enemy.name} starts with {enemy.health} HP.")
print(f"You start with {player.health} HP.")
answer = int(input("1-Attack, 2-Run away\n"))

if answer == 1:
    print("You begin to brawl...")
    while not player.is_dead() and not enemy.is_dead():
        attack = player.attack()
        enemy.health -= attack
        time.sleep(0.5)
        print(f"{player.name} hits {enemy.name} for {attack} HP! Enemy health: {enemy.health}")

        if enemy.is_dead():
            print(f"First time's the charm! Congratulations on your very first victory, {name}.")
            break

        attack = enemy.attack()
        player.health -= attack
        time.sleep(0.5)
        print(f"{enemy.name} hits {player.name} for {attack} HP! "
                f"Player health: {player.health}")
        time.sleep(0.5)

        if player.is_dead():
            print(f"{player.name} was defeated by {enemy.name}! Beautiful story.\nDEAD")
            sys.exit()

elif answer == 2:
    luck = random.randint(1, 20)
    if luck > 10:
        print("You managed to survive! *Phew*...")
    else:
        time.sleep(1)
        damage = random.randint(1, 10)
        player.health -= damage
        loss_gold = random.randint(1, max(1, player.gold // 2))
        player.gold -= loss_gold
        print(f"You flee, but not before getting hammered...\n"
              f"Your health dropped to {player.health}.")
        print(f"Your amount of money dropped to {loss_gold}. Current gold: {player.gold}.")
        time.sleep(1)
        if player.is_dead():
            print(f"Oops, {player.name} couldn't survive that.\nDEAD")
            sys.exit()
else:
    print("Wrong option!")
    sys.exit()

luck = random.randint(1, 20)
time.sleep(3)
print(f"You roll {luck}.")
time.sleep(0.5)
if luck > 13:
    print("You notice a few shiny coins lying on the ground before you!\nDo you pick them up?")
    time.sleep(2)
    answer = int(input("1-'Hell yeah!', 2-'No, I am a law-abiding citizen.'\n"))
    if answer == 1:
        coins = random.randint(3, 19)
        player.gold += coins
        print(f"Now we're talking!\nYour amount of money increased to {player.gold}.")
        time.sleep(2)
        player.update_alignment(chaotic_delta=1)
    elif answer == 2:
        print("Your willpower is enviable.")
        time.sleep(1.5)
        player.update_alignment(lawful_delta=1)

time.sleep(2)
print("That was... quite an eventful evening.")
time.sleep(2)
print("Your weariness grows while the sky slowly darkens above you.")
time.sleep(3)
print("Do you settle down in a camp or search for a tavern?\n1-Camp, 2-Tavern")
answer = int(input())
if answer == 1:
    time.sleep(0.5)
    print("You decide to spend the night united with nature, "
          "blissfully unaware of whatever dangers it harbours.")
    time.sleep(3)
    print("For now, it is.")
    time.sleep(0.8)
    player.restore_health()
    time.sleep(4)
elif answer == 2:
    print("It takes you a brief while to find a more or less neat tavern.")
    time.sleep(1)
    print("Nevertheless, you stride in confidently.")
else:
    print("Really now?")
    sys.exit()

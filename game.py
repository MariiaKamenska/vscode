import random
import sys
import time

class Player:
    def __init__(self, name, race, health=10, attack=(0,5), gold=0,
                 lawful=0, chaotic=0, good=0, evil=0, level=1, xp=0):
        self.name = name
        self.race = race
        self.max_health = health
        self.health = health
        self.attack = attack
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
        return self.health

    @health.setter
    def health(self, value):
        self.health = max(0, min(value, self.max_health))
        if self.health <= 0:
            print(f"{self.name} has fallen! Beautiful story.\nDEAD")

    def attack(self):
        min_attack = self.attack[0] + self.level
        max_attack = self.attack[1] + self.level * 2
        return random.randint(min_attack, max_attack)

    def restore_health(self):
        self.health = self.max_health
        print(f"{self.name} rests and restores health to {self.health}/{self.max_health} HP.")

    def gain_gold(self, amount):
        self.gold += amount
        print(f"{self.name} acquires {amount} gold. Total gold: {self.gold}.")

    def update_alignment(self, lawful_delta=0, chaotic_delta=0, good_delta=0, evil_delta=0):
        self.lawful += lawful_delta
        self.chaotic += chaotic_delta
        self.good += good_delta
        self.evil += evil_delta
        print(f"Alignment updated: Lawful {self.lawful}, Chaotic {self.chaotic}, Good {self.good}, Evil {self.evil}.")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP. Total XP: {self.xp}.")
        while self.xp >= self.next_level_xp:
            self.xp -= self.next_level_xp
            self.level += 1
            health_increase = int(5 * (self.level ** 0.5))
            self.max_health += health_increase
            time.sleep(1)
            print(f"{self.name} leveled up! Current level {self.level}, max health {self.max_health} HP.")
            time.sleep(1)
            self.next_level_xp = int(self.next_level_xp * 1.5)
            print(f"XP needed for next level: {self.next_level_xp}")


class Enemy:
    def __init__(self, name, player, base_health=(5,10), base_attack=(0,5)):
        self.name = name
        self.player = player
        self.base_health = base_health
        self.base_attack = base_attack
        self.health = base_health + (self.player.level * 9)

    def attack(self):
        min_attack = self.base_attack[0] + self.player.level
        max_attack = self.base_attack[1] + self.player.level * 2
        return random.randint(min_attack, max_attack)


print("Hello!")
name = str(input('Enter your name: '))
print(f"Nice name for our main character - {name}!")
print('Enter your race (from a capital)\n1-Human, 2-Orc, 3-Tiefling, 4-Dragonborn, 5-Elf')
input_race = int(input())
if input_race == 1:
    race = "Human"
elif input_race == 2:
    race = "Orc"
elif input_race == 3:
    race = "Tiefling"
elif input_race == 4:
    race = "Dragonborn"
elif input_race == 5:
    race = "Elf"
else:
    sys.exit("No game for you!")

player = Player(name, race, health=10, attack=(0,6))

city = input("Enter your city: ")
print(f'{player.name}, the {player.race} from {city}. Wondrous!')
time.sleep(2)
print(f"Your initial money supply consists of {player.gold} gold.")
time.sleep(3)
print("You begin as a Neutral character, but you will have all the freedom"
      "to bring changes as the story progresses.")
time.sleep(6)
print("Looks like you've stumbled upon an enemy...")
time.sleep(2)

enemies = ["Ogre", "Goblin", "Bandit", "Skeleton", "Dire Wolf", "Troll", "Drow"]
enemy_name = random.choice(enemies)
enemy = Enemy(enemy_name, player, base_health=random.randint(5, 10), base_attack=(0,5))

print(f"{enemy.name} blocks your path! Careful now!")
time.sleep(0.5)
print(f"{enemy.name} starts with {enemy.health} HP.")
print(f"You start with {player.health} HP.")
answer = int(input("1-Attack, 2-Run away\n"))

if answer == 1:
    print("You begin to brawl...")
    while player.health > 0 and enemy.health > 0:
        attack = player.attack()
        enemy.health -= attack
        time.sleep(0.5)
        print(f"{player.name} hits {enemy.name} for {attack} HP! Enemy health: {enemy.health}")

        if enemy.health > 0:
            enemy_attack = enemy.attack()
            player.health -= enemy_attack
            time.sleep(0.5)
            print(f"{enemy.name} hits {player.name} for {enemy_attack} HP! Player health: {player.health}")
            time.sleep(0.5)

    if player.health > 0 >= enemy.health:
        print(f"First time's the charm! Congratulations on your very first victory, {name}.")
    elif player.health <= 0 < enemy.health:
        print("You were defeated! Beautiful story.\nDEAD")

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
        print(f"You flee, but not before getting hammered...\nYour health dropped to {player.health}.")
        print(f"Your amount of money dropped to {loss_gold}. Current gold: {player.gold}.")
        time.sleep(1)
        if player.health <= 0:
            print(f"Oops, {player.name} couldn't survive that. \nDEAD")
else:
    print("Wrong option!")
    sys.exit()

luck = random.randint(1, 20)
time.sleep(3)
print(f"You roll {luck}.")
time.sleep(0.5)
if luck > 13:
    print("Woah! You notice a few shiny coins lying on the ground before you!\nDo you pick them up?")
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
    "Really now?"
    sys.exit()

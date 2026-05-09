import random
import sys
import time

from player import Player
from enemy import Enemy
from combat import fight


print("Hello! Choose the difficulty:\n1-Easy, 2-Normal, 3-Hard, 4-Masochist")
diff_choice = int(input())
diff_map = {1:'Easy', 2:'Normal', 3:'Hard', 4:'Masochist'}
difficulty = diff_map.get(diff_choice)
if difficulty is None:
    print("-_-")
    sys.exit()


name = str(input('Enter your name: '))
time.sleep(0.5)
print(f"Nice name for our main character - {name}!")
race_choice = int(input('Enter your race\n1-Human, 2-Orc, 3-Tiefling, 4-Dragonborn, 5-Elf: '))
race_map = {1:"Human",2:"Orc",3:"Tiefling",4:"Dragonborn",5:"Elf"}
race = race_map.get(race_choice)
if race is None:
    print("-_-")
    sys.exit()

gold = random.randint(0, 45)

player = Player(name=name, race=race, difficulty=difficulty, base_health=10, attack_range=(0, 6), gold=gold)
print(f"{player.name}, the {player.race}, starts with {player.health} HP and {player.gold} gold.")

# city = input("Enter your city: ")
# time.sleep(0.5)
# print(f'{player.name}, the {player.race} from {city}. Wondrous!')
# time.sleep(2)
time.sleep(3)
print("You begin as a Neutral character, but you will have all the freedom "
      "to bring changes as the story progresses.")
time.sleep(4)
print(f"Looks like {player.name} has stumbled upon an enemy...")
time.sleep(2)

enemies = ["Ogre", "Goblin", "Bandit", "Skeleton", "Dire Wolf", "Troll", "Drow"]
enemy_name = random.choice(enemies)
enemy = Enemy(enemy_name, player, base_health=(2, 5), base_attack=(0, 5))
fight(player, enemy)

luck = random.randint(1, 20)
time.sleep(3)
print(f"You roll {luck}.")
time.sleep(0.5)
if luck >= 12:
    print("You notice a few shiny coins lying on the ground before you!\nDo you pick them up?")
    answer = int(input("1-'Hell yeah!', 2-'No, I am a law-abiding citizen.'\n"))
    if answer == 1:
        coins = random.randint(3, 19)
        player.gold += coins
        print(f"Now we're talking!\nYour amount of money increased to {player.gold}.")
        time.sleep(2)
        player.chaotic += 1
    elif answer == 2:
        print("Your willpower is enviable.")
        time.sleep(1.5)
        player.lawful += 1
    else:
        print("-__-")
        sys.exit()

time.sleep(1)
print("That was... quite an eventful evening.")
time.sleep(2)
print("Your weariness grows while the sky slowly darkens above you.")
time.sleep(2)
print("Do you settle down in a camp or search for a tavern?\n1-Camp, 2-Tavern")
answer = int(input())
if answer == 1:
    time.sleep(0.5)
    print("You decide to spend the night united with nature, "
          "blissfully unaware of whatever dangers it harbours.")
    time.sleep(3)
    print("For now, it is.")
    time.sleep(1)
    player.restore_health()
elif answer == 2:
    print("It takes you a brief while to find a more or less neat tavern.")
    time.sleep(1)
    print("Nevertheless, you stride in confidently.")
    time.sleep(2)
    if player.race != 'Human':
        print("Your exotic appearance attracts a few stares.")
        luck = random.randint(1, 20)
        if luck < 7:
            time.sleep(1)
            print(".. and not all of them look friendly.")
    else:
        print("Nobody seems interested in you.")

    time.sleep(1)
    print("Do you take your time observing the surroundings or approach the bartender?")
    print("1-Observe, 2-Approach")
    answer = int(input())
    time.sleep(0.5)

    if answer == 1:
        print("The tavern looks pretty lively. The air is filled with humorous chatter, jarring music and a particularly acrious reek, especially aroud you.")
        time.sleep(4)
        if player.race != 'Human': 
            print("You notice a few people of your own kind among the present.")
            time.sleep(1)
            print("It is certainly reassuring.")
            time.sleep(2)

    print("You make your way towards the bar stand. The barkeep lifts his gaze at you lazily.")
    time.sleep(3)
    print("He drops polishing a mug - an attempt to look busy - and raises a brow.")
    time.sleep(2)

    if player.race != "Human":
        print("You catch the slighest hint of a frown on his expression as he picks up on your looks.")
        time.sleep(2)
    
    print("His tone is monotone, like the years of serving left each line memorised.")
    print(''':"Lookin' for somethin'? Drink, room, gossip?" ''')

    options = {
        1: {"name": "drink", "price": 1, "used": False},
        2: {"name": "room", "price": 5, "used": False},
        3: {"name": "gossip", "price": 3, "used": False}
    }

    done = False
    while not done:

        available = {
            k: v for k, v in options.items()
            if not v["used"]
        }

        if not available:
            print("The bartender has nothing more for you.")
            break

        for k, v in available.items():
            print(f"{k}-{v['name']}")

        answer = int(input("What do you ask for?\n"))

        if answer not in available:
            print("Invalid choice.")
            continue

        choice = available[answer]
        price = choice["price"]
        name = choice["name"]

        print("He extends his palm casually.")
        print(f':"{choice["price"]}"')
        pay = int(input("1-Pay up the price, 2-Refuse\n"))
        time.sleep(0.5)

        if pay == 1:
            if player.gold >= choice['price']:
                print("You hand in the gold.")
                player.gold -= choice['price']
                print(f"Your current gold coins: {player.gold}")
                choice["used"] = True

                if choice['name'] == "drink":
                    print("He retreats back to prepare the drink.")
                    
                elif choice['name'] == "room":
                    print("He hands you a key.")
                    done = True

                elif choice['name'] == "gossip":
                    time.sleep(1)
                    print("He leans closer, a grim expression suddenly appearing on his face.")
                    time.sleep(2)
                    print(''': "There's been a rumour lately... 'bout a certain wanderer..."''')
                    time.sleep(2)
                    print(''':"... who's so foolish..."''')
                    time.sleep(2)
                    print(''':"... that they're willing to part with gold for 'ome stupid tale!"''')
                    print("He lets out a rich laugh.")
                    time.sleep(1)

                    player.health -= 1
                    if player.health <= 1:
                        print("Your heart couldn't handle that level of viciousness!")
                        sys.exit()

                    print("You are left feeling slightly humiliated.")
                    print(f"You suffer a 1HP loss. Current HP: {player.health}")    

            else:
                print("Oops, not enough funds.")

        elif pay == 2: 
            print("You back away.")
            time.sleep(0.5)
            print("The man sighs.")
            time.sleep(1)
            continue

        else: 
            print("Bartender's had enough.")
            sys.exit()
    

else:
    print("Really now?")
    sys.exit()

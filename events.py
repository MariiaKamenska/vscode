import random
import time

def coin_event(player):

    luck = random.randint(1, 20)

    print(f"You roll {luck}.")

    if luck > 13:

        print("You notice coins on the road.")

        answer = int(input(
            "1-Take them\n"
            "2-Ignore them\n"
        ))

        if answer == 1:

            coins = random.randint(3, 19)

            player.gold += coins

            player.chaotic += 1

            print(f"You now have {player.gold} gold.")

        elif answer == 2:

            player.lawful += 1

            print("You leave the coins untouched.")
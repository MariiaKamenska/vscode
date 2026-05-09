import time
import sys
import random

def fight(player, enemy):

    print(f"{enemy.name} blocks your path!")

    while not player.is_dead() and not enemy.is_dead():

        print("1 - Attack")
        print("2 - Flee")
        answer = int(input())

        if answer == 1:

            damage = player.attack()

            enemy.health -= damage

            print(
                f"{player.name} hits "
                f"{enemy.name} for {damage} damage!"
            )

            time.sleep(0.5)

            if enemy.is_dead():

                print(f"{enemy.name} dies!")

                return

            damage = enemy.attack()

            player.health -= damage

            print(
                f"{enemy.name} hits "
                f"{player.name} for {damage} damage!"
            )

            time.sleep(0.5)

            if player.is_dead():

                print(f"{player.name} died.")

                sys.exit()

        elif answer == 2:
            luck = random.randint(1, 20)
            if luck > 10:
                print("You escaped!")
                return
            else:
                damage = random.randint(1, 20)
                player.health -= damage
                loss_gold = random.randint(1, max(1, player.gold // 2))
                player.gold -= loss_gold
                
                time.sleep(1)
                print("You flee, but suffer injuries.")
                time.sleep(0.5)
                print(f"You lose {loss_gold} gold.")
                time.sleep(0.5)
                print(f"Current HP: {player.health}.")

                if player.is_dead():
                    print(f"{player.name} did not survive.")
                    sys.exit()

                return
        
        else: 
            print("Wrong option.")
            sys.exit()



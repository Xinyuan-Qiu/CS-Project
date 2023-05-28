#Joe
import time
#making the slow motion of the word
import sys

import random


#making the slow motion of the word by making a function
def printSlow(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.045)


#Ashkan
print("\033[1;36;48m     x       x        x        x x x x x    x x x x x")
print("\033[1;36;48m     xx     xx       x x             x      x")
print("\033[1;36;48m     x x   x x      x x x          x        x x x x ")
print("\033[1;36;48m     x   x   x     x     x       x          x")
print("\033[1;36;48m     x       x    x       x    x x x x x    x x x x x")

print("")
print("")

print("\033[1;36;48m        xxxxx         x        x       x    x x x x x")
print("\033[1;36;48m      x              x x       xx     xx    x")
print("\033[1;36;48m     x     xxx      x x x      x x   x x    x x x x ")
print("\033[1;36;48m     x       x     x     x     x   x   x    x")
print("\033[1;36;48m      xxxxxxx     x       x    x       x    x x x x x")

print("")
print("")

printSlow("\033[1;31;48mWelcome to the maze game!!!\n")

name = input("\033[1;37;48mWhat is your name?\n").upper()

print(" ")

printSlow(
    f"Hi,{name},nice name by the way,are you ready to show off your skill?\n")

#Max
restart = 0
life = 3
turns = 0
player_energy = 100
monster_energy = 90

while restart == 0 and life > 0 and turns < 5 and monster_energy > 0:

    if player_energy <= 0:
        player_energy = 100

    if monster_energy < 90:
        monster_energy = 90

    print(" ")

    printSlow(
        "There are two types of weapons for you to choose: \nKnife = 0 \nLaser missle = 1\n"
    )

    print("")

    weapon_choice = int(input("Which one do you choose?\n"))

    weapon = ["knife", "laser_missle"]

    each_player_kill = 30

    each_monster_attack = 50

    if weapon_choice == 0:

        print(" ")

        printSlow("You got a knife on your way.\n")

        printSlow(
            "You are at the entrance and beginning to move forward >>>\n")

        print("")

        printSlow("There are two ways: \nLeft = 0 \nRight = 1\n")

        print("")

        pick_direction = int(input("Which direction do you want to go?\n"))

        print("")

        direction = ["left", "right"]

        #Joe + Ethan + Max + Ashkan

        if pick_direction == 0:
            printSlow(
                "Luckily, you arrive at a Recovery Centre, Engery level +50. \n1:You can try to go right next time. \n"
            )

            player_energy = player_energy + 50

            print("")

            print(f"You have {player_energy} energy now!")

            print("")

        elif pick_direction == 1:
            printSlow("Your met a monster.\n")

            print("")

            print("loading to see level bar\n")

            printSlow("...   ...   ...   ...   ...   ...   ...   ...   ... \n")

            print("")

            print(f"Monster energy: {monster_energy}  \nEach attack: 50\n")

            print("")

            print(f"Player engery: {player_energy}  \nEach kill: 30\n")

            while True:

                print("")

                print("")

                player_kill = input("Press k to kill: \n").lower()

                print("")

                if player_kill == "k":

                    printSlow("You kill the monster 30 energy off.\n")
                    printSlow("Monster attacks you 50 energy off.\n")

                    player_energy -= each_monster_attack

                    monster_energy -= each_player_kill

                    print("")

                    printSlow(f"Your remain engery:{player_energy}\n")

                    printSlow(f"Monster remain engery:{ monster_energy}\n")

                    if monster_energy <= 0 and player_energy >= 0:
                        print(
                            "You defeat the monster! congratulation!\n\033[1;31;48mGame is over!!!"
                        )

                        break

                    if monster_energy > 0 and player_energy <= 0:
                        print(" ")
                        print("You have no energy, dead...... \n")
                        print(" ")
                        
                        
#Ethan
                        life = life - 1

                        if life > 0:

                            print(
                                f"Luckily, you have {life} life remaining.\n1:You can try to go left next time. \n2:Choose laser missle. \n3:Come back to challenge the monster again.\n"
                            )

                            print(" ")
                            restart = int(input("Press 0 to restart:\n"))

                        elif life == 0:
                            print(
                                "Unfortunately, you have already taken three lifes\n\033[1;31;48mGame is over!!! \n"
                            )

                        break

#Max
    if weapon_choice == 1:
        printSlow("You got a laser missle on your way.\n")

        print("")

        print("You are at the entrance and began to move forward.")

        print("")

        printSlow(
            "UNLUCKILY, you met a gigantic monster\nand the laser missle has no bullets, you have to run!!!\n"
        )

        print("")

        printSlow("DON'T JUST STAND THERE.\nRUN FOR YOUR LIFE!!!\n")

        print("")

        #Joe
        while turns < 5:
            player_run = (input("press r to run: \n")).lower()

            if player_run == "r":

                print("")

                printSlow("There are two ways: \nLeft = 0 \nRight = 1\n")

                print("")

                run_direction = int(
                    input("Which direction do you want to go?\n"))

                print("")

                direction = ["left", "right"]

                monster_catch_possiblities = random.randrange(0, 4)

                if run_direction == monster_catch_possiblities:

                    printSlow(
                        "Um... The monster chooses the same direction with you \nYou are dead!!!"
                    )
                    print("")

                    #Ethan
                    life = life - 1

                    if life > 0:

                        print(" ")
                        printSlow(
                            f"Fortunately, you have {life} life remaining! ")
                        print("")

                        restart = int(input("press 0 to restart:\n"))

                    elif life == 0:
                        printSlow(
                            "Unfortunately, you have already taken three lifes\n\033[1;31;48mGame is over, try more times!!!"
                        )

                    break

#Joe
                elif run_direction != monster_catch_possiblities:

                    print(
                        "Continue to run.The monster haven't caught you yet!!!"
                    )

                    turns = turns + 1

                    if turns == 5:

                        print(" ")
                        printSlow(
                            "\033[1;31;48mjYou have successfully passed the maze. Congradulation!!!\n"
                        )

                        break

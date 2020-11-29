# File: AHSDoty.py
# Project: CSIS2101 Assignment 6
# Author: Mathew Doty
# History: Version 2.1 October 2, 2020

# This program will make a game
# that will have a player choose between three superheroes

# They will face the computer's randomly chosen superhero
# and see if they will win the battle

#import random module
import random

def AHSDoty():
    #specify how player will choose their hero
    print("Type A for Aqua Man")
    print("Type H for Human Torch")
    print("Type S for Swamp Thing")
    #superhero input
    hero = input("Please enter your choice of superhero (A, H, or S): ")
#validate input
    while hero != "A" and hero != "H" and hero != "S":
        print("Invalid input")
        hero = input("Please enter again (A, H, or S): ")
#input selection representations
    if hero == "A":
        hero = "Aqua Man"

    elif hero == "H":
        hero = "Human Torch"

    elif hero == "S":
        hero = "Swamp Thing"
#display chosen fighter
    print("You have chosen", hero)
#randomize enemy selection
    enemy = random.randrange(100, 301, 100)
    #enemy selection representations
    #*try making enemy choice different variable*
    if enemy == 100:
        enemy = "Aqua Man"
    elif enemy == 200:
        enemy = "Human Torch"
    elif enemy == 300:
        enemy = "Swamp Thing"
#display enemy fighter
    print("The enemy is", enemy)
#tie
    #*put into while loop instead*
    if enemy == hero:
        print("Tie, please play again.")
        #redo inputs for both
        AHSDoty()
#Show Aqua Man winner
    elif enemy == "Aqua Man" and hero == "Human Torch" or \
    enemy == "Human Torch" and hero == "Aqua Man":
        print("Aqua Man extinguishes Human Torch")
        print("Aqua Man wins")
#Show Human Torch winner
    elif enemy == "Human Torch" and hero == "Swamp Thing" or \
    enemy == "Swamp Thing" and hero == "Human Torch":
        print("Human Torch burns Swamp Thing")
        print("Human Torch wins")
#Show Swamp Thing winner
    elif enemy == "Swamp Thing" and hero == "Aqua Man" or \
    enemy == "Aqua Man" and hero == "Swamp Thing":
        print("Swamp Thing drowns Aqua Man")
        print("Swamp Thing wins")
#execute function
AHSDoty()

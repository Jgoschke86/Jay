import random
import os


choices = {0:0, 1:"Rock", 2:"Paper", 3:"Scissors"}
win = False

def cls():
    os.system("cls")

while True:
    while not win:
        choice = input("""1. Rock
2. Paper
3. Scissors
""")
        cls()
        comp_choice = random.choice(list(choices.values())[1:])
        if choice == "1":
            if comp_choice == "Rock":
                win = False
            if comp_choice == "Paper":
                win = False
            if comp_choice == "Scissors":
                win = True
        if choice == "2":
            if comp_choice == "Rock":
                win = True
            if comp_choice == "Paper":
                win = False
            if comp_choice == "Scissors":
                win = False
        if choice == "3":
            if comp_choice == "Rock":
                win = False
            if comp_choice == "Paper":
                win = True
            if comp_choice == "Scissors":
                win = False
        player_name = list(choices.values())[int(choice)]
        if win == False:
            print(player_name, " does not beat", str(comp_choice) + ", try again")
    print("Congrats! You have won")
    print(player_name, " does beat", str(comp_choice))
    again = input("Would you like to play again?  y/n   ")
    if again == "y":
        win = False
    else:
        break
from random import randint
import os

def cls():
    os.system("cls")
pause = False
cls()



# Scorecard [line number, label, value 1, value 2]
card = [[], [1, "Ones"], [2, "Twos"], [3, "Threes"], [4, "Fours"], [5, "Fives"], [6, "Sixes"], [7, "Three of a kind"], [8, "Four of a kind"], [9, "Full house"], [10, "Small straight"], [11, "Large straight"], [12, "Yahtzee"], [13, "Chance"], [14, "Yahtzee bonus"]]


welcome = input("""Please make a selection.
1. New Game
2. Exit
""")
cls()
if welcome == str(1):

    while pause != True:
        current_dice = []
        dice_roll = 5
        for x in range(0, dice_roll):
            current_dice.append(randint(1,6))
        saved_dice = []
        


        while True:
            print("Dice rolled - " + str(current_dice))
            print("Dice saved - " + str(saved_dice))                
            after_roll = int(input("""What would you like to do?
1. Roll again
2. Save dice.
3. Enter score.
4. See scorecard
"""))
            cls()
            if after_roll == 1:
                cls()
                break
            elif after_roll == 2:
                to_save = int(input("Please enter the number you would like to save. "))
                if to_save in current_dice:                          # Takes saved number and moves it to 
                    save = current_dice.index(to_save)               # saved_dice list
                    saved_dice.append(to_save)
                    current_dice.pop(save)
                    dice_roll -= 1
                    cls()
                else:
                    print("Not a valid number.")
                    cls()
            elif after_roll == 3:
                #  Prints card
                for i in range(1,14):
                    print(" ".join(map(str, card[i])))
                print("Dice - " + str(current_dice + saved_dice))
                selection = int(input("Where would you like to add your score? "))


                # Score input for 1-6
                if selection <= 6:
                    if len(card[selection]) == 2:
                        num = current_dice.count(selection) + saved_dice.count(selection)
                        total = selection * num
                        temp = card[selection]
                        temp.append(total)
                        card.pop(selection)
                        card.insert(selection,temp)
                        cls()
                        break
                    elif len(card[selection]) == 3:
                        num = current_dice.count(selection) + saved_dice.count(selection)
                        total = selection * num
                        temp = card[selection]
                        temp.append(total)
                        card.pop(selection)
                        card.insert(selection,temp)
                        cls()
                        break
                    else:
                        print("This number already has it's slots full. Please choose a different number.")


                # # 3 of a kind
                # if selection == 7:
                #     if len(card[7]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")

                # # 4 of a kind
                # if selection == 1:
                #     if len(card[1]) == 1:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     elif len(card[1]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")

                # # Full house
                # if selection == 1:
                #     if len(card[1]) == 1:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     elif len(card[1]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")

                # # Small straight
                # if selection == 1:
                #     if len(card[1]) == 1:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     elif len(card[1]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")

                # # Large straight
                # if selection == 1:
                #     if len(card[1]) == 1:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     elif len(card[1]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")

                # # Yahtzee
                # if selection == 1:
                #     if len(card[1]) == 1:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     elif len(card[1]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")
                # # Chance
                # if selection == 13:
                #     if len(card[13]) == 2:
                #         num = sum(dice_roll)
                #         card.append(num[13])
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")
                # # Yahtzee bonus
                # if selection == 1:
                #     if len(card[1]) == 1:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     elif len(card[1]) == 2:
                #         num = dice_roll.count(1)
                #         card.append(1 * num)
                #     else:
                #         print("This number already has it's slots full. Please choose a different number.")

            elif after_roll == 4:
                cls()
                #  Prints card
                for i in range(14):
                    print(" ".join(map(str, card[i])))
            
            else:
                print("Please enter valid selection.")



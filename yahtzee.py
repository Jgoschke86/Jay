from random import randint
import os

def cls():
    os.system("cls")
pause = False
cls()

def score_to_card():
    temp = card[selection]
    temp.append(total)
    card.pop(selection)
    card.insert(selection,temp)
def stat_clear():
    

# Scorecard line number, label, value 1, value 2
card = [[], [1, "Ones"], [2, "Twos"], [3, "Threes"], [4, "Fours"], [5, "Fives"], [6, "Sixes"], [7, "Three of a kind"], [8, "Four of a kind"], [9, "Full house"], [10, "Small straight"], [11, "Large straight"], [12, "Yahtzee"], [13, "Chance"], [14, "Yahtzee bonus"]]


welcome = input("""Please make a selection.
1. New Game
2. Exit
""")
cls()
if welcome == str(1):
    roll = 0                                # Keeps track of roll count
    current_dice = []                       # Current dice rolled
    saved_dice = []                         # Dice saved and not rerolled
    turn = 1                                # Keeps track of turn count, max 13
    dice_roll = 5                           # Number of dice to be rolled
    while turn != 14:
        
        
        if roll <= 2:    
            current_dice.clear()    
            for x in range(0, dice_roll):
                current_dice.append(randint(1,6))
            roll += 1
        else:
            print("You are out of rolls. Please place a score.")    
    
        while True:
            print(turn)
            print(roll)
            print("Dice rolled - " + str(current_dice))
            print("Dice saved - " + str(saved_dice))                
            after_roll = input("""What would you like to do?
1. Roll again
2. Save dice.
3. Enter score.
4. See scorecard
""")
            
            
            if after_roll == str(1):
                cls()
                break
            
            elif after_roll == str(2):
                to_save = int(input("Please enter the number you would like to save. "))
                if to_save in current_dice:                          # Takes saved number and moves it to saved_dice list
                    save = current_dice.index(to_save)
                    saved_dice.append(to_save)
                    current_dice.pop(save)
                    dice_roll -= 1
                    
                else:
                    pass
                cls()
            
            elif after_roll == str(3):
                for i in range(1,14):                                       #  Prints card
                    print(" ".join(map(str, card[i])))
                
                print("Dice - " + str(current_dice + saved_dice))
                selection = int(input("Where would you like to add your score? "))
                turn += 1

                
                if selection <= 6 and len(card[selection]) <= 3:                        # Score input for 1-6
                    num = current_dice.count(selection) + saved_dice.count(selection)
                    total = selection * num
                    score_to_card()
                    roll = 0
                    dice_roll = 5
                    saved_dice.clear()
                    cls()
                    break
                    
                


                # 3 of a kind
                if selection == 7:
                    if len(card[7]) == 2:
                        dice = current_dice + saved_dice
                        p = []
                        q = 1
                        for i in range(1,6):
                            p.append(dice.count(q))
                            q += 1
                        if 3 in p:
                            total = sum(current_dice + saved_dice)
                            score_to_card()
                        else:
                            zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                            if zero == "y":
                                total = 0
                                score_to_card()
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                cls()
                            else:
                                pass

                    else:
                        print("This number already has it's slots full. Please choose a different number.")

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
                else:
                    cls()
                    print("This number already has it's slots full. Please choose a different number.")
            elif after_roll == str(4):
                cls()
                #  Prints card
                for i in range(14):
                    print(" ".join(map(str, card[i])))
            
            else:
                print("Please enter valid selection.")



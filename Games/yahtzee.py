from random import randint
import os

def cls():
    os.system("cls")
def score_to_card_top():
    temp = card[selection]
    temp.append(total)
    top_btotal.append(total)
    card.pop(selection)
    card.insert(selection,temp)
def score_to_card_bottom():
    temp = card[selection]
    temp.append(total)
    bottom_total.append(total)
    card.pop(selection)
    card.insert(selection,temp)
    

# Scorecard line number, label, value 1, value 2
card = [[], [1, "Ones"], [2, "Twos"], [3, "Threes"], [4, "Fours"], [5, "Fives"], [6, "Sixes"], [7, "Three of a kind"], [8, "Four of a kind"], [9, "Full house"], [10, "Small straight"], [11, "Large straight"], [12, "Yahtzee"], [13, "Chance"], [14, "Yahtzee bonus"]]


cls()
while True:
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
        top_btotal = []                         # List to determine if bonus is earned
        top_bonus = []                          # Will contain bonus if eligible
        bottom_total = []                       # Stores bottom section numbers for total score

        while turn != 14:
            
            if roll <= 2:    
                current_dice.clear()    
                for x in range(0, dice_roll):
                    current_dice.append(randint(1,6))
                roll += 1
            else:
                print("You are out of rolls. Please place a score.")    
        
            while True:
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
                    

                    
                    if selection <= 6 and len(card[selection]) == 2:                        # Score input for 1-6
                        dice = current_dice.count(selection) + saved_dice.count(selection)
                        total = selection * dice
                        score_to_card_top()
                        roll = 0
                        dice_roll = 5
                        saved_dice.clear()
                        turn += 1
                        cls()
                        break
                    

                    # 3 of a kind
                    if selection == 7:
                        if len(card[7]) == 2:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                t = dice.count(q)
                                p.append(t)
                                q += 1
                            if 3 in p or 4 in p or 5 in p:
                                total = sum(current_dice + saved_dice)
                                score_to_card_bottom()
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                            else:
                                zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                                if zero == "y":
                                    total = 0
                                    score_to_card_bottom()
                                    roll = 0
                                    dice_roll = 5
                                    saved_dice.clear()
                                    turn += 1
                                    cls()
                                    break
                                else:
                                    cls()
                                    pass
                            
                        else:
                            cls()
                            print("This number already has it's slots full. Please choose a different number.")


                    # 4 of a kind
                    if selection == 8:
                        if len(card[8]) == 2:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                t = dice.count(q)
                                p.append(t)
                                q += 1
                            if 4 in p or 5 in p:
                                total = sum(current_dice + saved_dice)
                                score_to_card_bottom()
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                            else:
                                zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                                if zero == "y":
                                    total = 0
                                    score_to_card_bottom()
                                    roll = 0
                                    dice_roll = 5
                                    saved_dice.clear()
                                    turn += 1
                                    cls()
                                    break
                                else:
                                    pass
                            
                        else:
                            cls()
                            print("This number already has it's slots full. Please choose a different number.")


                    # Full house
                    if selection == 9:
                        if len(card[9]) == 2:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                t = dice.count(q)
                                p.append(t)
                                q += 1
                            if 2 and 3 in p:
                                total = 25
                                score_to_card_bottom()
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                            else:
                                zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                                if zero == "y":
                                    total = 0
                                    score_to_card_bottom()
                                    roll = 0
                                    dice_roll = 5
                                    saved_dice.clear()
                                    turn += 1
                                    cls()
                                    break
                                else:
                                    cls()
                                    pass
                            
                        else:
                            cls()
                            print("This number already has it's slots full. Please choose a different number.")


                    # Small straight
                    if selection == 10:
                        if len(card[10]) == 2:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                t = dice.count(q)
                                p.append(t)
                                q += 1
                            if p == [0, 1, 1, 1, 1] or p == [1, 1, 1, 1, 0]:
                                total = 30
                                score_to_card_bottom
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                            else:
                                zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                                if zero == "y":
                                    total = 0
                                    score_to_card_bottom()
                                    roll = 0
                                    dice_roll = 5
                                    saved_dice.clear()
                                    turn += 1
                                    cls()
                                    break
                                else:
                                    cls()
                                    pass
                        else:
                            print("This number already has it's slots full. Please choose a different number.")


                    # Large straight
                    if selection == 11:
                        if len(card[11]) == 2:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                t = dice.count(q)
                                p.append(t)
                                q += 1
                            if p == [1, 1, 1, 1, 1]:
                                total = 40
                                score_to_card_bottom
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                            else:
                                zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                                if zero == "y":
                                    total = 0
                                    score_to_card_bottom()
                                    roll = 0
                                    dice_roll = 5
                                    saved_dice.clear()
                                    turn += 1
                                    cls()
                                    break
                                else:
                                    cls()
                                    pass
                        else:
                            print("This number already has it's slots full. Please choose a different number.")


                    # Yahtzee
                    if selection == 12:
                        if len(card[12]) == 2:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                p.append(dice.count(q))
                                q += 1
                            if 6 in p:
                                total = 50
                                score_to_card_bottom()
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                            else:
                                zero = input("You don't have the proper dice for this. Would you like to enter a 0? y/n  ")
                                if zero == "y":
                                    total = 0
                                    score_to_card_bottom()
                                    roll = 0
                                    dice_roll = 5
                                    saved_dice.clear()
                                    turn += 1
                                    cls()
                                    break
                                else:
                                    cls()
                                    pass
                            
                        else:
                            cls()
                            print("This number already has it's slots full. Please choose a different number.")


                    # Chance
                    if selection == 13:
                        if len(card[13]) == 2:
                            dice = current_dice + saved_dice
                            total = sum(dice)
                            score_to_card_bottom()
                            roll = 0
                            dice_roll = 5
                            saved_dice.clear()
                            turn += 1
                            cls()
                            break
                        else:
                            cls()
                            print("This number already has it's slots full. Please choose a different number.")


                    # Yahtzee Bonus
                    if selection == 14:
                        if len(card[12]) >= 2 and len(card[12]) == 3:
                            dice = current_dice + saved_dice
                            p = []
                            q = 1
                            for i in range(0,6):
                                t = dice.count(q)
                                p.append(t)
                                q += 1
                            if 6 in p:
                                total = 100
                                score_to_card_bottom()
                                while True:
                                    print("You must also input a normal score.")
                                    print("Dice - " + str(current_dice + saved_dice))
                                    selection = int(input("Where would you like to add your score? "))
                                    if selection <= 6 and len(card[selection]) == 2:                        # Score input for 1-6
                                        dice = current_dice + saved_dice
                                        total = sum(dice)
                                        score_to_card_top()
                                        roll = 0
                                        dice_roll = 5
                                        saved_dice.clear()
                                        turn += 1
                                        cls()
                                        break
                                    # 3 of a kind
                                    if selection == 7:
                                        if len(card[7]) == 2:
                                            dice = current_dice + saved_dice
                                            total = sum(dice)
                                            score_to_card_bottom()
                                            roll = 0
                                            dice_roll = 5
                                            saved_dice.clear()
                                            turn += 1
                                            cls()
                                            break
                                        
                                        else:
                                            cls()
                                            print("This number already has it's slots full. Please choose a different number.")


                                    # 4 of a kind
                                    if selection == 8:
                                        if len(card[8]) == 2:
                                            dice = current_dice + saved_dice
                                            total = sum(dice)
                                            score_to_card_bottom()
                                            roll = 0
                                            dice_roll = 5
                                            saved_dice.clear()
                                            turn += 1
                                            cls()
                                            break
                                        
                                        else:
                                            cls()
                                            print("This number already has it's slots full. Please choose a different number.")


                                    # Full house
                                    if selection == 9:
                                        if len(card[9]) == 2:
                                                total = 25
                                                score_to_card_bottom()
                                                roll = 0
                                                dice_roll = 5
                                                saved_dice.clear()
                                                turn += 1
                                                cls()
                                                break
                                        else:
                                            cls()
                                            print("This number already has it's slots full. Please choose a different number.")


                                    # Small straight
                                    if selection == 10:
                                        if len(card[10]) == 2:
                                                total = 30
                                                score_to_card_bottom
                                                roll = 0
                                                dice_roll = 5
                                                saved_dice.clear()
                                                turn += 1
                                                cls()
                                                break
                                        else:
                                            print("This number already has it's slots full. Please choose a different number.")


                                    # Large straight
                                    if selection == 11:
                                        if len(card[11]) == 2:
                                                total = 40
                                                score_to_card_bottom
                                                roll = 0
                                                dice_roll = 5
                                                saved_dice.clear()
                                                turn += 1
                                                cls()
                                                break
                                        else:
                                            print("This number already has it's slots full. Please choose a different number.")
                                    # Chance
                                    if selection == 13:
                                        if len(card[13]) == 2:
                                            dice = current_dice + saved_dice
                                            total = sum(dice)
                                            score_to_card_bottom()
                                            roll = 0
                                            dice_roll = 5
                                            saved_dice.clear()
                                            turn += 1
                                            cls()
                                            break
                                        else:
                                            cls()
                                            print("This number already has it's slots full. Please choose a different number.")
                                roll = 0
                                dice_roll = 5
                                saved_dice.clear()
                                turn += 1
                                cls()
                                break
                        else:
                            cls()
                            print("You are not able to do this right now.")


                    # Top section bonus
                    if len(top_btotal) == 6:
                        s = sum(top_btotal)
                        if s >= 63:
                            top_bonus.append(35)
                    
                elif after_roll == str(4):
                    cls()
                    #  Prints card
                    for i in range(14):
                        print(" ".join(map(str, card[i])))
                
                else:
                    cls()
                    print("Please enter valid selection.")


        top_btotal.extend(top_bonus)
        top_btotal.extend(bottom_total)
        grand_total = sum(top_btotal)
        print("Game over! Your final score was " + str(grand_total))

        
    else:
        break
    





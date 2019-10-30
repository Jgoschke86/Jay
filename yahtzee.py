from random import randint


dice_roll = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
saved_dice = []
final_dice = saved_dice.extend(dice_roll)




# Scorecard [line number, label, value 1, value 2]
card = [[1, "Ones"], [2, "Twos"], [3, "Threes"], [4, "Fours"], [5, "Fives"], [6, "Sixes"], [7, "Three of a kind"], [8, "Four of a kind"], [9, "Full house"], [10, "Small straight"], [11, "Large straight"], [12, "Yahtzee"], [13, "Chance"], [14, "Yahtzee bonus"]]

#  Prints card
for i in range(14):
    ind = 0
    print(" ".join(map(str, card[i])))
    ind += 1
selection = 1


# Score input for 1-6
if selection <= 6:
    if len(card[selection]) == 2:
        num = dice_roll.count(selection)
        card.append(int(selection) * num)
    elif len(card[selection]) == 3:
        num = dice_roll.count(selection)
        card.append(int(selection) * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")


# 3 of a kind
if selection == 7:
    if len(card[7]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")

# 4 of a kind
if selection == 1:
    if len(card[1]) == 1:
        num = dice_roll.count(1)
        card.append(1 * num)
    elif len(card[1]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")

# Full house
if selection == 1:
    if len(card[1]) == 1:
        num = dice_roll.count(1)
        card.append(1 * num)
    elif len(card[1]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")

# Small straight
if selection == 1:
    if len(card[1]) == 1:
        num = dice_roll.count(1)
        card.append(1 * num)
    elif len(card[1]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")

 # Large straight
if selection == 1:
    if len(card[1]) == 1:
        num = dice_roll.count(1)
        card.append(1 * num)
    elif len(card[1]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")

# Yahtzee
if selection == 1:
    if len(card[1]) == 1:
        num = dice_roll.count(1)
        card.append(1 * num)
    elif len(card[1]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")
# Chance
if selection == 13:
    if len(card[13]) == 2:
        num = sum(dice_roll)
        card.append(num[13])
    else:
        print("This number already has it's slots full. Please choose a different number.")
# Yahtzee bonus
if selection == 1:
    if len(card[1]) == 1:
        num = dice_roll.count(1)
        card.append(1 * num)
    elif len(card[1]) == 2:
        num = dice_roll.count(1)
        card.append(1 * num)
    else:
        print("This number already has it's slots full. Please choose a different number.")


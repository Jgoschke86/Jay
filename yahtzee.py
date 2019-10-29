from random import randint


dice_roll = randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)





card = [["Ones", 0, 0], ["Twos", 0, 0], ["Threes", 0, 0], ["Fours", 0, 0], ["Fives", 0, 0], ["Sixes", 0, 0], ["Bonus", 0], ["Three of a kind", 0], ["Four of a kind", 0], ["Full house", 0], ["Small straight", 0], ["Large straight", 0], ["Yahtzee", 0], ["Chance", 0], ["Yahtzee bonus", 0, 0]]

#  prints card
for i in range(15):
    ind = 0
    print(" ".join(map(str, card[i])))
    ind += 1
selection = 1




if selection == 1:
    if len.card[1] == 1:
        ones = dice_roll.count(1)
        card.append(1 * ones)
    elif len.card[1] == 2:
        ones = dice_roll.count(1)
        card.append(1 * ones)
    else:
        print("This number already has it's slots full. Please choose a different number.")


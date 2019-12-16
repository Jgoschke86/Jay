import random
import os






cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",]

def new_card():
    card = random.choice(cards)
    cards.remove(card)
    return card

def pcard_total():
    for card in p_cards:
        if card == "J":
            p_cards.remove("J")
            p_cards.append(10)
        if card == "Q":
            p_cards.remove("Q")
            p_cards.append(10)
        if card == "K":
            p_cards.remove("K")
            p_cards.append(10)
        if card == "A":
            p_cards.remove("A")
            if sum(p_cards) > 21:
                p_cards.append(1)
            else:
                p_cards.append(11)
        total += card
    score = sum(total)
    return score
            
while True:
 
    p_turn = 0
    p_cards = []
    c_turn = 0
    c_cards = []
    game_on = True


    p_cards.append(new_card())
    p_cards.append(new_card())
    c_cards.append(new_card())
    while game_on:
        print(p_cards)
        print(c_cards)
        print(pcard_total)
        turn_select = input("What would you like to do?\n 1. Hit\n 2. Stay\n 3. Quit\n ")
        if turn_select == "1":
            p_cards.append(new_card())
        elif turn_select == "2":
            continue
        elif turn_select == "3":
            game_on = False
        else:
            print("Please enter a valid selection of 1, 2, or 3")
    
    break

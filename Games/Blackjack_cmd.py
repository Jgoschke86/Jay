import random
import os



p_turn = 0

c_turn = 0
turn = True
game_on = True


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",]

def new_card():
    card = random.choice(cards)
    cards.remove(card)
    return card


            
while game_on:
 
    p_cards = []
    c_cards = []
    score = 0
    p_cards.append(new_card())
    p_cards.append(new_card())
    c_cards.append(new_card())
    while score <= 21:
        score = 0
        for card in p_cards:
            if card == "J":
                score += 10
            elif card == "Q":
                score += 10
            elif card == "K":
                score += 10
            elif card == "A":
                if score > 10:
                    score += 1
                else:
                    score += 11
            else:
                score += card
        

        
        print(score)
        print(p_cards)
        print(c_cards)
        turn_select = input("What would you like to do?\n 1. Hit\n 2. Stay\n 3. Quit\n ")
        if turn_select == "1":
            p_cards.append(new_card())
            score = 0
        elif turn_select == "2":
            continue
        elif turn_select == "3":
            game_on = False
            break
        else:
            print("Please enter a valid selection of 1, 2, or 3")
        
        if new_card() == "J":
            score += 10
        elif new_card() == "Q":
            score += 10
        elif new_card() == "K":
            score += 10
        elif new_card() == "A":
            if score > 10:
                score += 1
            else:
                score += 11
        else:
            score += int(new_card())
        print(score)
        print(p_cards)
        print(c_cards)
    while score > 21:
            print("You lose!")
            play_again = input("Would you like to play again? y/n ")
            if play_again == "y":
                turn = False
                break
            if play_again == "n":
                game_on = False
                turn = False
                break
            else:
                print("Not a valid answer, please answer \"y\" or \"n\"")
                
    
    

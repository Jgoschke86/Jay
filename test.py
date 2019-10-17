play = True
#Player inputs word to guess
while play == True:
    word = input("What word would you like? ")
    letter = []
    dash = []

    
    #Seperates word into seperate letters in list letter
    for x in word:
        letter.append(x)
    
    
    #Converts letters into _ for dash list
    for x in letter:
        dash.append("_")
    
    #Guessing starts
    while True:
        print("The word is:")
        print(" ".join(map(str, dash)))
        
        if letter.count("@") == len(letter):
            break
        
        else:
            guess_letter = input("What letter would you like to guess? ")
        
        
        
            if guess_letter not in letter:
                print("Not in the word, please guess again")
        
        
            elif guess_letter in letter:
                print("Nice! That letter is in the word. Keep going!")
                while True:
                    if guess_letter in letter:
                        correct = letter.index(guess_letter)
                        dash[correct] = guess_letter
                        letter[correct] = "@"
                    else:
                        break
                
    print("Congratulations! You won!")
    again = input("Would you like to play again?")
    print(again)
    if again == "y" or "yes":
        print("Ok then")
        play == True
    else:
        again == "n" or "no"
        print("Thanks for playing!!")
        play == False
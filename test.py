
import os

def cls():
    os.system("cls")



#Player inputs word to guess
while True:
    word = input("What word would you like? ")
    letter = []
    dash = []
    already_guessed = []
    guess_count = 0
    cls()
    #Seperates word into seperate letters in list letter
    for x in word:
        letter.append(x)
    
    
    #Converts letters into _ for dash list
    for x in letter:
        dash.append("_")
    
    #Guessing loop
    while True:
        
        print("The word is:")
        print(" ".join(map(str, dash)))
        
                    #Checks to see if any letters are still available and ends guess loop if none
        if letter.count("@") == len(letter):
            break
            
                    #Player guesses letter
        else:
            guess_letter = input("What letter would you like to guess? ")
            cls()
            print("You have guessed " + str(guess_letter))
            
                    #Checks to see if letter has already been guessed or if in word
            if guess_letter not in letter:
                if guess_letter in already_guessed:
                    print("You have already guessed that letter. Please choose a different letter.")
                    print("You have already guessed " + str(already_guessed))
                    guess_count += 1
                else:
                    already_guessed.append(guess_letter)    #Adds letter to list
                    already_guessed.sort()
                    print("Not in the word, please guess again")
                    guess_count += 1
        
            #If in word
            elif guess_letter in letter:
                print("Nice! That letter is in the word!")
                while True:
                    if guess_letter in letter:
                        correct = letter.index(guess_letter)
                        dash[correct] = guess_letter        #Converts dash to letter
                        letter[correct] = "@"               #Converts letter in "letter list" to @
                        guess_count += 1
                        already_guessed.append(guess_letter)#Adds letter to list
                        already_guessed.sort()
        
                    else:
                        break
                
    print("Congratulations! You won!")
    print("It took you " + str(guess_count) + " guesses!")
    again = input("Would you like to play again? y/n ")
    
    if (again == "y"):
        print("Ok then")
    elif (again == "yes"):
        print("Ok then")
    elif (again == "no"):
        print("Thanks for playing!!")
        break
    elif (again == "n"):
        print("Thanks for playing!!")
        break

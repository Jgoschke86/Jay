
import os

def cls():
    os.system("cls")



#Player inputs word to guess
while True:
    word = input("What word would you like? ").lower()
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
            guess_letter = input("What letter would you like to guess? ").lower()
            cls()
            print("You have guessed " + str(guess_letter))
            
                    #Checks to see if letter has already been guessed or if in word
            if guess_letter not in letter:
                if guess_letter in already_guessed:
                    print("You have already guessed that letter. Please choose a different letter.")
                    print("Letters already guessed " + str(already_guessed))

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
    cls()            
    print("Congratulations! You won!")
    print("The word was " + word)
    if guess_count == 1:
        print("It took you " + str(guess_count) + " guess!")
    else:
        print("It took you " + str(guess_count) + " guesses!")
    
    
    pagain = ["y", "yes"]
    nagain = ["n", "no"]
    breaker = False
    while True:
        again = input("Would you like to play again? y/n ").lower()
        if again in nagain:
            print("Thanks for playing!!")
            breaker = True
            break
        elif again in pagain:
            break
        else:
            print("Please enter a valid response.")
    if breaker:
        break
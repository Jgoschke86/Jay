word = input("What word would you like? ")
letter = []
dash = []


for x in word:
    letter.append(x)

for x in letter:
    dash.append("_")



while True:
    print("The word is:")
    print(" ".join(map(str, dash)))
    guess_letter = input("What letter would you like to guess? ")
    
    
    if guess_letter not in letter:
        print("Not in the word, please guess again")
    
    
    elif guess_letter in letter:
        print("Nice! That letter is in the word. Keep trying!")
        correct = letter.index(guess_letter)
        dash[correct] = guess_letter
        

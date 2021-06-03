do_undo = input("""1.Convert to cipher
2.Undo Cipher
""")


def split_word(word):
    return [char for char in word]

#  Converts input into Cipher
if do_undo == "1":
    user_word = input("what do you want encrypted?  ")
    user_cipher = input("what cipher do you want?   ")

    #  Alphabet, altered letters based on ciper number, location of capital letters, location of letters in alpha, altered location based on cipher, join method
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_word = []
    is_cap = []
    loc = []
    new_loc = []
    s = ""

    split_string = split_word(user_word)
    shift = int(user_cipher)

    #  Converts letters to numerical location in alphabet and checks for capitalization
    for letter in split_string:
        if letter.lower() in abc:
            loc.append(abc.index(letter.lower()))
        else:
            loc.append(letter)
        if letter.isupper() == True:
            is_cap.append(split_string.index(letter))

    #  Converts to new alphabet location
    for i in loc:
        is_int = isinstance(i, int)
        if is_int == True:
            new_num = i + shift
            if new_num > 26:
                new_num = new_num % 26
        else:
            new_num = i
        new_loc.append(new_num)

    #  Converts new location to letters
    for num in new_loc:
        is_int = isinstance(num, int)
        if is_int == True:
            new_letter = abc[num]
            new_word.append(new_letter)
        else:
            new_word.append(num)

    #  Converts letters back into capitals
    for cap_loc in is_cap:
        word = new_word[cap_loc]
        new_word[cap_loc] = word.upper()

    #  Joins letters to make new sentence
    new_sent = s.join(new_word)
    print(new_sent)



#  Converts cipher back to normal
if do_undo == "2":
    og_word = input("""What do you want undone?
""")

    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    is_cap = []
    count = 1
    loc = []
    split_string = split_word(og_word)

    #  Converts letters to numerical location in alphabet and checks for capitalization
    for letter in split_string:
        if letter.lower() in abc:
            loc.append(abc.index(letter.lower()))
        else:
            loc.append(letter)
        if letter.isupper() == True:
            is_cap.append(split_string.index(letter))

    for i in range(27):
        new_word = []
        new_loc = []
        s = ""

        #  Converts to new alphabet location
        for i in loc:
            is_int = isinstance(i, int)
            if is_int == True:
                new_num = i + count
                print(new_num)
                if new_num >= 26:
                    new_num = new_num - 25
                else:
                    new_num + 8
                print(new_num)
            else:
                new_num = i
            new_loc.append(new_num)

        #  Converts new location to letters
        for num in new_loc:
            is_int = isinstance(num, int)
            if is_int == True:
                new_letter = abc[num]
                new_word.append(new_letter)
            else:
                new_word.append(num)

        #  Converts letters back into capitals
        for cap_loc in is_cap:
            word = new_word[cap_loc]
            new_word[cap_loc] = word.upper()

        #  Joins letters to make new sentence
        new_sent = s.join(new_word)
        print(count)
        print(new_sent)
        count += 1



abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

aba = ""
for i in range(len(abc)):
    letter = abc[i]
    aba = aba + letter + aba
    print(aba)
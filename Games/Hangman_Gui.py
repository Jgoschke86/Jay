from tkinter import *



root = Tk()
root.title("Hangman")
root.config(bg = "blue")

alpha1 = ["A", "B", "C", "D", "E", "F"]
alpha2 = ["G", "H", "I", "J", "K", "L"]
alpha3 = ["M", "N", "O", "P", "Q", "R"]
alpha4 = ["S", "T", "U", "V", "W", "X"]
alpha5 = ["Y", "Z"]

dash_word = StringVar()
letters_guessed = StringVar()
man_shape = StringVar()

dash_word.set("Test")
letters_guessed.set("  ".join(map(str, alpha1)) + "\n" + "  ".join(map(str, alpha2)) + "\n" + "  ".join(map(str, alpha3)) + "\n" + "  ".join(map(str, alpha4)) + "\n" + "  ".join(map(str, alpha5)))
man_shape.set("test2")


word_box = Label(root, textvariable = dash_word, width = 30)
word_box.config(font = 20, relief = SUNKEN)
word_box.grid(row = 1, column = 1, columnspan = 3)

guess_box = Label(root, textvariable = letters_guessed, width = 15, height = 8, relief = SUNKEN)
guess_box.config(font = 20)
guess_box.grid(row = 3, column = 1)

man_box = Label(root, textvariable = man_shape, width = 15, height = 8, relief = SUNKEN)
man_box.config(font = 20)
man_box.grid(row = 3, column = 3)

# Top row
blankbox1 = Label(root, height = 2, bg = "blue")
blankbox1.grid(row = 0, column = 0, columnspan = 4)
# Left side column
blankbox2 = Label(root, width = 2, bg = "blue")
blankbox2.grid(row = 1, column = 0, rowspan = 2)
# Center column
blankbox3 = Label(root, width = 2, bg = "blue")
blankbox3.grid(row = 2, column = 2, rowspan = 2)
# Right side column
blankbox4 = Label(root, width = 2, bg = "blue")
blankbox4.grid(row = 1, column = 4, rowspan = 2)
# Word and box spacer, row 3 spacer
blankbox5 = Label(root, height = 2, bg = "blue")
blankbox5.grid(row = 2, column = 1, columnspan = 4)
# Bottom row
blankbox6 = Label(root, height = 2, bg = "blue")
blankbox6.grid(row = 4, column = 1, columnspan = 4)

root.mainloop()
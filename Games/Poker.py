from tkinter import *
import random


# ♠♣♥♦

root = Tk()
root.title("Black Jack")
root.configure(bg = "green")


pcard1 = Label(text = "1\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
pcard2 = Label(text = "1\n2", width = 3, height = 2, relief = SUNKEN, bg = "white")
pcard3 = Label(text = "3\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
pcard4 = Label(text = "4\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
pcard5 = Label(text = "5\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
pcard6 = Label(text = "6\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")

ccard1 = Label(text = "1\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
ccard2 = Label(text = "2\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
ccard3 = Label(text = "3\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
ccard4 = Label(text = "4\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
ccard5 = Label(text = "5\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")
ccard6 = Label(text = "6\n♠", width = 3, height = 2, relief = SUNKEN, bg = "white")

pcard1.config(font=("Courier", 44))
pcard2.config(font=("Courier", 44))
pcard3.config(font=("Courier", 44))
pcard4.config(font=("Courier", 44))
pcard5.config(font=("Courier", 44))
pcard6.config(font=("Courier", 44))
ccard1.config(font=("Courier", 44))
ccard2.config(font=("Courier", 44))
ccard3.config(font=("Courier", 44))
ccard4.config(font=("Courier", 44))
ccard5.config(font=("Courier", 44))
ccard6.config(font=("Courier", 44))


pcard1.grid(row = 1, column = 2)
pcard2.grid(row = 1, column = 3)
pcard3.grid(row = 1, column = 4)
pcard4.grid(row = 1, column = 5)
pcard5.grid(row = 1, column = 6)
pcard6.grid(row = 1, column = 7)
ccard1.grid(row = 3, column = 2)
ccard2.grid(row = 3, column = 3)
ccard3.grid(row = 3, column = 4)
ccard4.grid(row = 3, column = 5)
ccard5.grid(row = 3, column = 6)
ccard6.grid(row = 3, column = 7)


new = Button(text = "New Game", width = 12)
hit = Button(text = "Hit", width = 12)
stay = Button(text = "Stay", width = 12)
over = Button(text = "Quit", width = 12, command = root.destroy)
new.grid(row = 5, column = 3)
hit.grid(row = 5, column = 4)
stay.grid(row = 5, column = 5)
over.grid(row = 5, column = 6)


blank1 = Label(height = 2, bg = "green")
blank2 = Label(height = 2, bg = "green")
blank3 = Label(height = 2, bg = "green")
blank4 = Label(height = 2, bg = "green")
blank5 = Label(width = 2, bg = "green")
blank6 = Label(width = 2, bg = "green")
blank1.grid(row = 0, column = 0, columnspan = 7)
blank2.grid(row = 2, column = 0, columnspan = 7)
blank3.grid(row = 4, column = 0, columnspan = 7)
blank4.grid(row = 6, column = 0, columnspan = 7)
blank5.grid(row = 0, column = 0, rowspan = 7)
blank6.grid(row = 0, column = 8, rowspan = 7)

root.mainloop()
from tkinter import *
import random


# ♠♣♥♦

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suit = ["♠", "♣", "♥", "♦"]
pcard = ["", "", "", "", "", ""]
ccard = ["", "", "", "", "", ""]
used_cards = []
pturn = 0
cturn = 0


root = Tk()
root.title("Black Jack")
root.configure(bg = "green")


if pturn == 0:
    pcard[0] = str(random.choice(value)) + "\n" + random.choice(suit)
    pcard[1] = str(random.choice(value)) + "\n" + random.choice(suit)
    ccard[0] = str(random.choice(value)) + "\n" + random.choice(suit)
    pturn += 1


p1 = StringVar()
p2 = StringVar()
p3 = StringVar()
p4 = StringVar()
p5 = StringVar()
p6 = StringVar()
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
c4 = StringVar()
c5 = StringVar()
c6 = StringVar()

p1.set(pcard[0])
p2.set(pcard[1])
p3.set(pcard[2])
p4.set(pcard[3])
p5.set(pcard[4])
p6.set(pcard[5])
c1.set(ccard[0])
c2.set(ccard[1])
c3.set(ccard[2])
c4.set(ccard[3])
c5.set(ccard[4])
c6.set(ccard[5])

#   Player cards
p_card1 = Label(textvariable = p1, width = 3, height = 2, relief = SUNKEN, bg = "white")
p_card2 = Label(textvariable = p2, width = 3, height = 2, relief = SUNKEN, bg = "white")
p_card3 = Label(textvariable = p3, width = 3, height = 2, relief = SUNKEN, bg = "white")
p_card4 = Label(textvariable = p4, width = 3, height = 2, relief = SUNKEN, bg = "white")
p_card5 = Label(textvariable = p5, width = 3, height = 2, relief = SUNKEN, bg = "white")
p_card6 = Label(textvariable = p6, width = 3, height = 2, relief = SUNKEN, bg = "white")
#   Computer cards
c_card1 = Label(textvariable = c1, width = 3, height = 2, relief = SUNKEN, bg = "white")
c_card2 = Label(textvariable = c2, width = 3, height = 2, relief = SUNKEN, bg = "white")
c_card3 = Label(textvariable = c3, width = 3, height = 2, relief = SUNKEN, bg = "white")
c_card4 = Label(textvariable = c4, width = 3, height = 2, relief = SUNKEN, bg = "white")
c_card5 = Label(textvariable = c5, width = 3, height = 2, relief = SUNKEN, bg = "white")
c_card6 = Label(textvariable = c6, width = 3, height = 2, relief = SUNKEN, bg = "white")



#   Card font
p_card1.config(font=("Courier", 44))
p_card2.config(font=("Courier", 44))
p_card3.config(font=("Courier", 44))
p_card4.config(font=("Courier", 44))
p_card5.config(font=("Courier", 44))
p_card6.config(font=("Courier", 44))
c_card1.config(font=("Courier", 44))
c_card2.config(font=("Courier", 44))
c_card3.config(font=("Courier", 44))
c_card4.config(font=("Courier", 44))
c_card5.config(font=("Courier", 44))
c_card6.config(font=("Courier", 44))

#   Placement of cards
p_card1.grid(row = 3, column = 2)
p_card2.grid(row = 3, column = 3)
p_card3.grid(row = 3, column = 4)
p_card4.grid(row = 3, column = 5)
p_card5.grid(row = 3, column = 6)
p_card6.grid(row = 3, column = 7)
c_card1.grid(row = 1, column = 2)
c_card2.grid(row = 1, column = 3)
c_card3.grid(row = 1, column = 4)
c_card4.grid(row = 1, column = 5)
c_card5.grid(row = 1, column = 6)
c_card6.grid(row = 1, column = 7)

#   Bottom buttons
new = Button(text = "New Game", width = 12)
hit = Button(text = "Hit", width = 12)
stay = Button(text = "Stay", width = 12)
over = Button(text = "Quit", width = 12, command = root.destroy)
new.grid(row = 5, column = 3)
hit.grid(row = 5, column = 4)
stay.grid(row = 5, column = 5)
over.grid(row = 5, column = 6)

#   Labels to take up space to seperate everything
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
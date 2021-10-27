#!/usr/bin/python3

from tkinter import *

def doit():
   b1.configure(text="Ouch!")

top = Tk()

b1 = Button (top,text="Push Me",command=doit)
b1.pack()


top.mainloop()

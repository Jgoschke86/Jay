#!/usr/bin/python3

from tkinter import *

# make button b1 red (no parameters)
def turnRed():
    b1.configure(activebackground='red')
    b1.configure(background='red')

top = Tk()

b1 = Button(top,text="Push Me (red)",command=turnRed)
b1.pack()

bye = Button(top,text="Exit", command=top.destroy)
bye.pack()

top.mainloop()  

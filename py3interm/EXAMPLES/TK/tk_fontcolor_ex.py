#!/usr/bin/python3

from tkinter import *

bigcode = ( "Courier",48,"bold" )  

top = Tk()

label_one = Label(top,text="This is label ONE",font=bigcode)
label_one.pack()


label_two = Label(
    top,
    text="This is the SECOND label",
    foreground="yellow",
    background="darkblue",
    activeforeground="#0CAA59",
    activebackground="darkblue",
)
label_two.pack()

label_three = Label(top,text="This is label three",font=bigcode)
label_three.pack()

label_three.configure(font="-*-Helvetica-Bold-R-Normal--*-180-*-*-*-*-*-*")

mybutton = Button(top,text="Push Me",command=top.destroy)
mybutton.configure( font=("Times", 36, "italic"))
mybutton.pack()

top.mainloop()


#!/usr/bin/python3

from tkinter import *

# create a toplevel window
top = Tk()
top.title("Hello from Tkinter")

lab_hello = Label(top,text="Hello, Tkinter World") 
lab_hello.configure(foreground="yellow",background='blue')
lab_hello.pack()

b_exit = Button(top,text="Quit",command=top.destroy)
b_exit.pack()

top.mainloop()
